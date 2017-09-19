import zmq
context = zmq.Context.instance()
receiver = context.socket(zmq.PAIR)
receiver.bind("ipc://step2")
msg = receiver.recv()
print msg
