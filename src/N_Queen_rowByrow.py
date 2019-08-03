#!/usr/bin/python3

global N

def print_board(board):
    global N
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N, 1)):
        if board[i][j] == 1:
            return False

    return True


def solve_N_Queen(board, row):
    global N
    if row >= N:
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve_N_Queen(board, row+1):
                return True

            board[row][col] = 0

    return False


def main():
    global N
    while True:
        N = int(input("Enter The Number of Queen: "))

        board = []

        for i in range(N):
            board.append([])
            for j in range(N):
                board[i].append(0)

        if solve_N_Queen(board, 0) == False:
            print("Solution Doesn't Exist.")

        print_board(board)
        print()



if __name__ == '__main__':
    main()