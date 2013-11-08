from headhunter import HunterManager, HunterRunner

global_runner = None
global_counter = 0

def test_integration():
  global global_runner
  
  config = dict(
    amqp_server = '0.0.0.0', queue_name = 'test-task-queue'
  )
  
  closed_over_value = 1
  my_name = __name__
  
  def without_closure():
    pass
  
  def with_exception():
    raise ValueError
  
  def background_job():
    import sys
    sys.modules[my_name].global_counter = closed_over_value
    sys.modules[my_name].global_runner.halt_processing()
  
  global_runner = HunterRunner(**config)
  manager = HunterManager(**config)
  
  manager.enqueue(with_exception)
  manager.enqueue(without_closure)
  
  closed_over_value = 2
  manager.enqueue(background_job)
  closed_over_value = 3
  
  import select
  try:
    global_runner.run()
  except select.error:
    pass
  
  assert global_counter == 2, "{0} != 1".format(global_counter)

if __name__ == '__main__':
  test_integration()