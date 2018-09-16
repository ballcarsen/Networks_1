def read_board(file_name):
    with open(file_name) as file:
        next(file) #skips first row of the file since its all numbers anyway
        #reads in file and adds to 2d array unsure how to ingore the first character though so just cheating and +1 when I need x
        board_array = [line.split() for line in file]
        return board_array

def save_board(file_name, board_array):
    with open(file_name, "w") as f:
        f.write("  0 1 2 3 4 5 6 7 8 9")
        for r in board_array:
            f.write("\n")
            for c in r:
                f.write(str(c) + " ")

def check_board(x, y, board_array):
    char_at_pos = board_array[y][x+1]
    if char_at_pos == '_':
        board_array[y][x+1] = "O"
        return [board_array, 200, 'hit=0']
    elif char_at_pos == 'X' or char_at_pos == "O":
        return [board_array, 410]
    else:
        board_array[y][x+1] = "X"
        C_count = sum(x.count('C') for x in board_array)
        B_count = sum(x.count('B') for x in board_array)
        R_count = sum(x.count('R') for x in board_array)
        S_count = sum(x.count('S') for x in board_array)
        D_count = sum(x.count('D') for x in board_array)
        counts = [C_count, B_count, R_count, S_count, D_count]
        if all(count == 0 for count in counts):
            return [board_array, 200, 'hit=1&sink=%s' % char_at_pos, True]
        else:
            if sum(x.count(char_at_pos) for x in board_array) == 0:
                return [board_array, 200, 'hit=1&sink=%s' % char_at_pos]
            else:
                return [board_array, 200, 'hit=1']

def update_board(x, y,  board_array, character):
    board_array[x][y+1] = character
    return board_array

#Client side can call process_request(x, y, file_name, character = O or X) and it will update the board
def process_request(x, y, file_name, character = None):
    board_array = read_board(file_name)
    #Changes the character at position x,y
    if character:
        board_array = update_board(x,y, board_array, character)
        save_board(file_name, board_array)
        return(True)
    else:
        results = check_board(x, y, board_array)
        save_board(file_name, results[0])
        return results[1:]

if __name__ == '__main__':
    print(process_request(0,5, 'own_board.txt'))










