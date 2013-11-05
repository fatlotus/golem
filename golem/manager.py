from pika import BlockingConnection, ConnectionParameters
import sys
import yaml
import marshal

class GolemManager(object):
  def __init__(self, amqp_server, queue_name):
    self.parameters = ConnectionParameters(amqp_server)
    self.queue_name = queue_name
    
    self.connection = BlockingConnection(self.parameters)
    self.channel = self.connection.channel()
    
    self.channel.queue_declare(self.queue_name,
      durable = True)
    
  def enqueue(self, function):
    request = marshal.dumps(function.func_code)
    
    self.channel.basic_publish(
      exchange = '',
      routing_key = self.queue_name,
      body = request
    )

if __name__ == '__main__':
  def hello_world_function():
    print "Hello, world!"
  
  config_file = os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__, 'configuration.yaml' ))))
  sys.exit(GolemRunner(**yaml.load(open(config_file))).
    enqueue(hello_world_function))