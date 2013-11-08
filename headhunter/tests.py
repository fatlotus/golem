from headhunter import HunterManager, HunterRunner

def test_integration():
  config = dict(
    amqp_server = '0.0.0.0', queue_name = 'task-queue'
  )
  
  def function_a():
    raise Exception("worksa")
  
  def function_b():
    raise Exception("worksb")
  
  def function_c():
    raise Exception("worksc")
  
  manager = HunterManager(**config)
  manager.enqueue(function_a)
  manager.enqueue(function_b)
  
  runner = HunterRunner(**config)
  
  try:
    runner.run()
  except Exception, e:
    assert str(e) == "worksa"
  
  try:
    runner.run()
  except Exception, e:
    assert str(e) == "worksb"
  
  manager.enqueue(function_c)
  
  try:
    runner.run()
  except Exception, e:
    assert str(e) == "worksc"