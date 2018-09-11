import socket
import sys


def make_connection(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('10.152.142.15', port))
    s.listen(1)
    conn, addr = s.accept()
    data = conn.recv(64)
    print(data)
    conn.send(data)
    conn.close()


if __name__ == '__main__':
    port = int(sys.argv[1])
    file_name = sys.argv[2]
    make_connection(port)