import sys
from settings import NetworkSettings
from http.server import BaseHTTPRequestHandler, HTTPServer
from flask import Flask, render_template



class BattleshipServer(BaseHTTPRequestHandler):
    #POST
    def do_POST(self):
        length = int(self.headers["Content-Length"])
        print("Data: " + str(self.rfile.read(length), "utf-8"))

        response = bytes("Response", "utf-8")

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

    server = HTTPServer((ip, port), BattleshipServer)
    server.serve_forever()

app = Flask(__name__)

#Hosts the own board
@app.route('/own_board.html')
def display_own():
    display("own_board")

#Hosts the opponent board
@app.route('/opponent_board.html')
def display():
    display("opponent_board")

#Reads the text of a board and renders a template
def display(name):
    app.run(debug=True)
    text = open(name + '.txt', 'r+')
    content = text.read()
    text.close()
    return render_template(name + '.html', text=content)



if __name__ == '__main__':
    network_settings = NetworkSettings()
    port = int(sys.argv[1])
    file_name = sys.argv[2]
    #0 for Brodcast IP, 1 for local ip
    use_local = int(sys.argv[3])

    #Starts the flask app to host the boards
    app.run(debug=True, use_reloader=False)

    make_connection(port, network_settings, use_local)
