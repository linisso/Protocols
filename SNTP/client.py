import socket
import time

import ntplib

try:
    ntp = ntplib.NTPClient().request('ntp2.stratum2.ru')
    print('Real time: ' + time.ctime(ntp.tx_time))
    ntp2 = ntplib.NTPClient().request('127.0.0.1', port=123)
    print('False time: ' + time.ctime(ntp2.tx_time))
except:
    print('Server is not working')
