import zmq
context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind('tcp://*:5557')
while True:
    data = raw_input('input your data:')
    socket.send(data)
