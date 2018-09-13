from flask import Flask, render_template
from flask_classful import FlaskView, route

app = Flask(__name__)


class Board:
    def __init__(self, file_name):
        self.file_name = file_name

    @app.route('/own_board.html')
    def display(self):
        app.run(debug=True)
        text = open('own_board.txt', 'r+')
        content = text.read()
        text.close()
        return render_template('board.html', text=content)


if __name__ == '__main__':
    board = Board('input.txt')
    board.display()