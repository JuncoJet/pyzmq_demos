import zmq
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('ipc://test')
socket.setsockopt(zmq.SUBSCRIBE,'')
while True:
    data = socket.recv()
    print data
