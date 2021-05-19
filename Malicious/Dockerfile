FROM ubuntu:20.04

RUN apt update && apt install -y python3 python3-pip iproute2

RUN pip3 install scapy

COPY generate.py /generate.py

CMD python3 /generate.py