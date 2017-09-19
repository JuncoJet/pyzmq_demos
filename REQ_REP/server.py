import zmq
import time
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://*:5555')
while True:
    data = socket.recv()
    print data
    time.sleep(1)
    socket.send('ok')
