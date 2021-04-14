import time
import socket
import random

HOST = 'cmsc614-project-demo_server_1'
PORT = 31337

time.sleep(1)

while True:
    message_content = b"Hello Friend"

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            for _ in range(10):
                print("Sending message: %s" % message_content)
                s.sendall(message_content)
                data = s.recv(1024)
                print("Received: " + str(data))
                time.sleep(1)
    except:
        pass
    finally:
        time.sleep(5)