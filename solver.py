import time

calls = 0

def main(board):

    global calls
    calls = 0
    print_board(board)

    start = time.perf_counter()
    solved = solve(board)
    end = time.perf_counter()

    print()

    print_board(board)
    print(f"Execution time: {end - start:.6f} seconds")
    print(f"Recursive calls: {calls}")

    return solved


def print_board(board):
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            print(num, end=" ")

        print()


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    else:
        return None


def valid(row, col, num, board):
    # check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # check col
    for i in range(9):
        if board[i][col] == num:
            return False

    # check 3x3
    grid_row = (row // 3) * 3
    grid_col = (col // 3) * 3
    for i in range(grid_row, grid_row + 3, 1):
        for j in range(grid_col, grid_col + 3, 1):
            if board[i][j] == num:
                return False
    else:
        return True


def solve(board):
    global calls
    calls += 1
    # find empty spot

    empty = find_empty(board)
    if empty is None:
        return True
    else:
        x, y = empty

    # try all numbers 1-9
    for num in range(1, 10):
        if valid(x, y, num, board):
            board[x][y] = num
            if solve(board):
                return True
            else:
                board[x][y] = 0

    return False


if __name__ =="__main__":
    board = [
        [0, 3, 0, 0, 0, 1, 0, 2, 4],
        [0, 0, 7, 0, 0, 5, 1, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 8, 0],
        [7, 0, 0, 0, 1, 0, 6, 9, 0],
        [4, 0, 0, 0, 3, 8, 0, 0, 0],
        [0, 0, 2, 5, 0, 0, 0, 0, 1],
        [0, 0, 1, 3, 4, 2, 9, 0, 0],
        [0, 6, 5, 0, 9, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 3, 7]
    ]

    main(board)
