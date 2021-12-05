#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('04.txt', 'r') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

# ==== SOLUTION ====
total = 0

numbers = [int(x) for x in rows[0].split(",")]

boards = []

board = []
for row in rows[2:]:
    if len(row) == 0:
        boards.append(board)
        board = []
    nums = [[int(x), 0] for x in row.split()]
    if nums:
        board.append(nums)
boards.append(board)


def setboard(number, board):
    for row in board:
        for col in row:
            if col[0] == number:
                col[1] = 1


def checkboard(board):
    # check rows
    for row in board:
        tot = 0
        for col in row:
            tot += col[1]
        if tot >= 5:
            return True

    for i in range(5):
        tot = 0
        for row in board:
            tot += row[i][1]
        if tot >= 5:
            return True
    return False


def printboard(board):
    for row in board:
        print()
        for col in row:
            mark = "x" if col[1] else " "
            print(f"({mark} {col[0]:2})", end=" ")
    print()


def sumwinner(board, current):
    tot = 0
    for row in board:
        for col in row:
            if not col[1]:
                tot += col[0]
    return current * tot


for number in numbers:
    newboards = []
    for board in boards:
        setboard(number, board)
        if not checkboard(board):
            newboards.append(board)
        elif len(boards) == 1:
            print(sumwinner(boards[0], number))
    boards = newboards
