import zmq
import time
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://*:5555')
while True:
    data = raw_input('input your data:')
    socket.send(data)
