#!/usr/bin/python3
import sys

"""This module has a solution to n queens problem"""


def is_safe(board, row, col, n):
    """
    function checks if a queen can be placed at the given position
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def Queens(board, col, n):
    """
      function is a recursive function that tries to place a queen
       in all cells of a given column

    """
    if col >= n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            Queens(board, col + 1, n)
            board[i][col] = 0


def main():
    """
    This is a program the solve N Queens puzzle
    Usage: nqueens N
    N: is the number of queens, length and width of the board
    """

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0]*n for _ in range(n)]
    Queens(board, 0, n)


if __name__ == "__main__":
    main()
