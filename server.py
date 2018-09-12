import socket
import sys
from settings import NetworkSettings
from http.server import BaseHTTPRequestHandler, HTTPServer


class BattleShipServer(BaseHTTPRequestHandler):
    #POST
    def do_POST(self):
        length = int(self.headers["Content-Length"])
        print("Data: " + str(self.rfile.read(length), "utf-8"))

        response = bytes("This is the response.", "utf-8")  # create response

        self.send_response(200)
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()

        self.wfile.write(response)

def make_connection(port, network_settings, use_local):
    if use_local == 0:
        ip = network_settings.IP
        print("using %s as IP address" % network_settings.IP)
    elif use_local == 1:
        ip = network_settings.LOCAL_IP
        print("using %s as IP address" % network_settings.LOCAL_IP)
    else:
        print("Wrong IP choice value")
        return(False)

    server = HTTPServer((ip, port), BattleShipServer)
    server.serve_forever()



if __name__ == '__main__':
    network_settings = NetworkSettings()
    port = int(sys.argv[1])
    file_name = sys.argv[2]
    #0 for Brodcast IP, 1 for local ip
    use_local = int(sys.argv[3])
    make_connection(port, network_settings, use_local)