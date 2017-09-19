import zmq
context = zmq.Context()
recive = context.socket(zmq.PULL)
recive.connect('tcp://localhost:5557')
sender = context.socket(zmq.PUSH)
sender.connect('tcp://localhost:5558')
while True:
    data = recive.recv()
    sender.send(data)
