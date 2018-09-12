import netifaces as ni
import socket



class NetworkSettings:
    def __init__(self):
        ni.ifaddresses('en0')
        self.IP = ni.ifaddresses('en0')[ni.AF_INET][0]['addr']
        ni.ifaddresses('lo0')
        print("IP address: " + self.IP)
        self.LOCAL_IP = socket.gethostbyname('localhost')
        print("Local IP: " + self.LOCAL_IP)