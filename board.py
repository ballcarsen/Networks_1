class Board:
    hits = 0
    def __init__(self, file_name):
        self.file_name = file_name

    with open("input.txt") as file:
        next(file) #skips first row of the file since its all numbers anyway
        board_array = [line.split() for line in file] #reads in file and adds to 2d array unsure how to ingore the first character though so just cheating and +1 when I need x


    def update_board(self, x, y, file):#updates board array checks win if hit, returns true if the game should be over
        if(self.board_array[x][y+1] != '_' and self.board_array[x][y+1] != "O"):
            self.board_array[x][y+1]='X'
            self.hits+=1
            if(self.hits == 4):#update 4 to max hits possible
                with open(file, "w") as f:
                    f.write("Game Over")
                return True
        else:
            self.board_array[x][y+1] = 'O'
        with open(file, "w") as f:
            f.write("  0 1 2 3 4 5 6 7 8 9")
            for r in self.board_array:
                f.write("\n")
                for c in r:
                    f.write(str(c) + " ")




if __name__ == '__main__':
    board = Board('input.txt')
    board.update_board(1,1,"input.txt")
    board.update_board(4,5,"input.txt")
    board.update_board(5,4,"input.txt")
    board.update_board(5,4,"input.txt")
    board.update_board(5,3,"input.txt")
    board.update_board(5,6,"input.txt")





