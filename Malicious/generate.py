import time
import socket
import random

HOST = 'cmsc614-project-demo_server_1'
PORT = 31337

time.sleep(1)


i=0
while True:
    message_content = b"Hello World! %d" % i
    i += 1

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print("Sending message: %s" % message_content)
            s.sendall(message_content)
            data = s.recv(1024)
            print("Received: " + str(data))
    except Exception as e:
        print(e)
    finally:
        time.sleep(1)
