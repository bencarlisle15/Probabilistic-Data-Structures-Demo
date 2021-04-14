import socket
import time
from cuckoo_filter import CuckooFilter
from stable_bloom_filter import StableBloomFilter
from threading import Thread

HOST = '0.0.0.0'
PORT = 31337

INITIAL_ALLOWED_HOSTS = ["192.168.48.3"]

def init_filter(filter_type):
    if filter_type == 0:
        current_filter = CuckooFilter(table_size=10)
    else:
        current_filter = StableBloomFilter(5,24,7,10,7)
    for host in INITIAL_ALLOWED_HOSTS:
        current_filter.insert(host)
    return current_filter

def is_invalid_connection(current_filter, addr):
    host, port = addr
    return host not in current_filter

def single_connection(current_filter, conn, addr):
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print("Received: " + str(data))
            if not data:
                break
            if len(data) > 0:
                current_filter.insert(data)
                time.sleep(1)
                conn.sendall(b"Connection Allowed!")

current_filter = init_filter(1)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        if is_invalid_connection(current_filter, addr):
            conn.close()
            continue
        Thread(target=single_connection, args=[current_filter, conn, addr]).start()