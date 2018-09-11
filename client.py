import socket
import sys
import urllib
import httplib2


def make_connection(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
   # s.send(bytes('POST ...'))
    conn = httplib2.Http(ip)
    resp, content = h.request(ip)
    assert resp.status
    conn.request("POST", "hello")
    r = conn.getresponse()
    data = r.read()

    conn.close()
    data = s.recv(64)
    '''params = urllib.urlencode(
        {
            'spam': 1, 'eggs': 2, 'bacon':0
        }
    )

     f = urllib.urlopen("http://" + ip + "?%s" % params)
    s.send(bytes('POST 1'))
    data = f.read()'''
    print (data)

    s.close()


if __name__ == '__main__':
    ip = sys.argv[1]
    port = int(sys.argv[2])
#    x = sys.argv[3]
#    y = sys.argv[4]

    make_connection(ip, port)