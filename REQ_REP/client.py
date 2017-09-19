import zmq
import time
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:5555')
while True:
    data = raw_input('input your data:')
    socket.send(data)
    response = socket.recv()
    print response
