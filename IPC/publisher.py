import zmq
import time
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('ipc://test')
while True:
    data = raw_input('input your data:')
    socket.send(data)
