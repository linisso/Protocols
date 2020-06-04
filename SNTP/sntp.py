import socket

import ntplib


def get_current_time():
    client = ntplib.NTPClient()
    response = client.request('ntp2.stratum2.ru')
    return response


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 123))

while True:
    data, client = server.recvfrom(1024)
    correction = int(open('config.txt').read())
    response = get_current_time()
    response.recv_timestamp += correction
    response.tx_timestamp += correction
    server.sendto(response.to_data(), client)
