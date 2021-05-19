import socket
import re

from cuckoopy import CuckooFilter
from stable_bloom_filter import StableBloomFilter
from threading import Thread

HOST = '0.0.0.0'
PORT = 31337

print(socket.gethostbyname("cmsc614-project-demo_semihonest_1"))

INITIAL_ALLOWED_HOSTS = [socket.gethostbyname("cmsc614-project-demo_semihonest_1")]
unaddable_hosts = [socket.gethostbyname("cmsc614-project-demo_malicious_1")]

def init_filter(filter_type, hosts):
    if filter_type == 0:
        current_filter = CuckooFilter(capacity=2048, bucket_size=2048)
    else:
        current_filter = StableBloomFilter(5,22,7,10,7)
    for host in hosts:
        current_filter.insert(host)
    return current_filter

allowed_hosts = init_filter(0, INITIAL_ALLOWED_HOSTS)

def is_valid_connection(host):
    return host in allowed_hosts

def single_connection(conn, addr):
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode('utf-8')
            print("Received: " + str(data))
            if data and re.search("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", data):
                if data in unaddable_hosts:
                    print("Cannot add blocked ips")
                    conn.sendall(b"You cannot add this ip!")
                    continue
                # don't need to readd
                if not is_valid_connection(data):
                    try:
                        allowed_hosts.insert(data)
                        print("Adding ip: %s" % data)
                        conn.sendall(b"Connection Added!")
                    except:
                        print("Could not insert into filter!")
                        conn.sendall(b"Connection Could not be Added")
                else:
                    print("Ip already added")
                    conn.sendall(b"Connection Already Added!")
            else:
                conn.sendall(b"Thank you for your data")
                print("No ip")
                break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        host, port = addr
        if not is_valid_connection(host):
            print("Blocked!")
            conn.sendall(b"BLOCKED!")
            conn.close()
            continue
        Thread(target=single_connection, args=[conn, addr]).start()
