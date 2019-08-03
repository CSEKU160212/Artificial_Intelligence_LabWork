#!/usr/bin/python3
global N

def print_board(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


def is_safe_place(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_NQueen(board, col):
    if col >= N:
        return True

    for row in range(N):
        if is_safe_place(board, row, col):
            board[row][col] = 1

            if solve_NQueen(board, col+1):
                return True

            board[row][col] = 0
    return False


def main():
    global N
    while True:
        N = int(input("Please Enter The number of Queen: "))

        board = []
        for i in range(N):
            board.append([])
            for j in range(N):
                board[i].append(0)

        if solve_NQueen(board, 0) == False:
            print("Solution Doesn't Exists")
            print()

        print_board(board)
        print()



if __name__ == '__main__':
    main()