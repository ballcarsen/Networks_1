import socket
import sys
import requests
import urllib
import httplib2

def make_connection(IP, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, port))
    return(s)
    #todo send POST command

def send_message(s, IP, port):
    headers = """\
    POST /auth HTTP/1.1\r
    Content-Type: {content_type}\r
    Content-Length: {content_length}\r
    Host: {host}\r
    Connection: close\r
    \r\n"""

    body = "x=5&y=6"
    body_bytes = body.encode('ascii')
    header_bytes = headers.format(
        content_type="application/x-www-form-urlencoded",
        content_length=len(body_bytes),
        host=str(IP) + ":" + str(port)
     ).encode('iso-8859-1')
    to_send = header_bytes + body_bytes
    s.send(to_send)
    s.close()
    print(to_send)


if __name__ == '__main__':
    IP = sys.argv[1]
    port = int(sys.argv[2])
    s = make_connection(IP, port)
    send_message(s, IP, port)