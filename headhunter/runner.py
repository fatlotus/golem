from pika import BlockingConnection, ConnectionParameters, exceptions
import types
import pickle
import marshal
import traceback

def _make_cell(value):
  def inner(): return value
  return inner.func_closure[0]

class HunterRunner(object):
  def __init__(self, amqp_server, queue_name):
    self.parameters = ConnectionParameters(amqp_server)
    self.queue_name = queue_name
    self.done = False
    self.connection = None
  
  def halt_processing(self):
    if self.connection:
      self.connection.close()
  
  def process(self, channel, method, properties, body):
    try:
      packet = pickle.loads(body)
      closure = tuple(_make_cell(x) for x in packet[0])
      code_object = marshal.loads(packet[1])
      generated_function = types.FunctionType(code_object,
                             globals(), '<network>', closure = closure)
      
      generated_function()
    except:
      traceback.print_exc()
    finally:
      channel.basic_ack(delivery_tag = method.delivery_tag)
  
  def run(self, *argv):
    self.connection = BlockingConnection(self.parameters)
    self.channel = self.connection.channel()
    
    try:
      self.channel.queue_declare(self.queue_name, durable = True)
      self.channel.basic_consume(self.process, queue = self.queue_name)
    except exceptions.ConnectionClosed:
      pass
    finally:
      if not self.connection.is_closed:
        self.connection.close()