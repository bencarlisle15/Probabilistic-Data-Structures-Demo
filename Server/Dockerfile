FROM ubuntu:20.04

RUN apt update && apt install -y python3 python3-pip iproute2

RUN pip3 install scapy cuckoopy bitarray

COPY receive.py /receive.py
COPY stable_bloom_filter.py /stable_bloom_filter.py

CMD python3 /receive.py