import sys
import board
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import re

# Board file name
global file_name

# Battleship server
class BattleshipServer(BaseHTTPRequestHandler):

    # Creates and hosts the requested board
    def do_GET(self):

        html_name = str(self.path).replace("/", "")
        txt_name = html_name.replace(".html", ".txt")
        text = open(txt_name, 'r')

        print(txt_name)
        print(html_name)
        with open(html_name, "w") as out:
            out.write("<!DOCTYPE html>\n")
            out.write('<h2>Battle Ship!</h2>\n')
            out.write('<table style="width:10%">\n')
            out.write("<tr>\n")
            out.write("<th>#</th>\n")
            y = True

            for line in text.readlines():
                line = line.split()
                if y:
                    for i in line:
                        out.write("<th>%s</th>\n" % i)
                    y = False
                else:
                    out.write("<tr>")
                    for i in line:
                        out.write("<td>%s</td>\n" % i)
                out.write("</tr>")

            out.write("</p>\n</body>\n</html>")

        f = open(html_name, 'rb')

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f.read())

    # Processes and responds to a fire request
    def do_POST(self):

        length = int(self.headers["Content-Length"])
        raw_data = str(self.rfile.read(length), "utf-8")
        data = raw_data.replace("x", "")
        data = data.replace("y", "")
        data = data.replace("=", "")
        data = data.split("&")
        end_game = False
        params = {}
        r = re.compile('x=\d&y=\d')

        # if coordinates are out of bounds
        if int(data[0]) > 9 or int(data[0]) < 0 or int(data[1]) > 9 or int(data[1]) < 0:
            response = 404
        # If fire message not formatted in the correct way
        elif r.match(raw_data) is None:
            response = 400
        # Process the data
        else:
            result = board.process_request(int(data[0]), int(data[1]), file_name)
            response = result[0]
            if len(result) == 2:
                params = {'hit': result[1]}
            elif len(result) == 3:
                params = {'hit': result[1], 'sink': result[2]}
            elif len(result) == 4:
                params = {'hit': result[1], 'sink': result[2]}
                end_game = True

        # Send the response
        self.send_response(response, urllib.parse.urlencode(params))
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        if end_game:
            print('end game')
            self.close_connection

# Makes the server
def make_connection(port, ip):
    server = HTTPServer((ip, port), BattleshipServer)
    server.serve_forever()


if __name__ == '__main__':
    # Port from user
    port = int(sys.argv[1])
    # File name from user
    file_name = sys.argv[2]
    # Creates the connection
    make_connection(port, '127.0.0.1')
