import zmq
context = zmq.Context.instance()
sender = context.socket(zmq.PAIR)
sender.connect("inproc://step2")
message="step1 ready"
sender.send(message)
