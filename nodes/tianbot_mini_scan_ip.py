#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import socket
import threading

from numpy import true_divide

def get_ip_x():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

if __name__ == '__main__':    
    sock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock_server.bind(('192.168.8.149', 5000))


    cmd = '*:*:echo'
    sock_server.sendto(bytes(cmd, encoding='utf-8'), ('192.168.8.255', 5000))

    sock_server.settimeout(1)
    while True:
        try:
            data, addr = sock_server.recvfrom(1024)
            print(data, addr)
        except socket.timeout:
            print('time out')
            break
