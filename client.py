import socket
import sys
import http.client
import urllib.parse


def send_message(ip, port, x, y, local):
    params = urllib.parse.urlencode({"x": x, "y": y})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    #If not locally hosting
    if local == 0:
        conn = http.client.HTTPConnection(ip, port)
    elif local == 1:
        conn = http.client.HTTPConnection(socket.gethostbyname('localhost'), 1040)
    else:
        print("No Connection Made")

    conn.request("POST", "", params, headers)
    response = conn.getresponse()
    data = response.reason

    if 'hit' in data and 'sink' in data:
        print('sink')
    elif 'hit' in data:
        print('hit')
    conn.close()


if __name__ == '__main__':
    ip = sys.argv[1]
    port = int(sys.argv[2])
    x = int(sys.argv[3])
    y = int(sys.argv[4])
    local = int(sys.argv[5])

    send_message(ip, port, x, y, local)