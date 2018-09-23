import socket
import sys
import http.client
import urllib.parse
import board


# Sends a message
def send_message(ip, port, x, y):
    # Formats the parameters
    params = urllib.parse.urlencode({"x": x, "y": y})
    # Headers for http message
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    # Creates the connection
    conn = http.client.HTTPConnection(ip, port)
    # Sends the post message
    conn.request("POST", "", params, headers)
    # HTTP Response from server
    response = conn.getresponse()
    data = response.reason
    print(data)
    print(response.status)

    # Process the response and update the opponent board
    if 'sink' in data:
        data = data.replace("hit=", "")
        data = data.replace("sink=", "")
        data = data.split('&')
        print('Sunk %s' % data[1])
        board.process_request(x,y, 'opponent_board.txt', 'X')
    elif 'hit' in data:
        print(data)
        data = int(data.replace("hit=", ""))
        if data == 0:
            board.process_request(x, y, 'opponent_board.txt', 'O')
        elif data == 1:
            board.process_request(x, y, 'opponent_board.txt', 'X')
    conn.close()


if __name__ == '__main__':
    # Ip address of server
    ip = sys.argv[1]
    # Port of server
    port = int(sys.argv[2])
    # X and Y coordinates
    x = int(sys.argv[3])
    y = int(sys.argv[4])
    # Sends the fire message and processes the response
    send_message(ip, port, x, y)