import socket
import random
import time

HOST = 'cmsc614-project-demo_server_1'
PORT = 31337

time.sleep(1)

r = random.Random()
r.seed(1337)

def create_random_ip():
    i_0 = r.randrange(255)
    i_1 = r.randrange(255)
    i_2 = r.randrange(255)
    i_3 = r.randrange(255)
    return b"%d.%d.%d.%d" % (i_0, i_1, i_2, i_3)

while True:

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            while True:
                message_content = create_random_ip()
                print("Sending: %s" % message_content)
                s.sendall(message_content)
                data = s.recv(1024)
                print("Received: %s" % data)
    except Exception as e:
        print(e)
    finally:
        time.sleep(0.1)
