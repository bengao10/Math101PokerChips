#############################
## Written by Benjamen Gao
## For Math 101 Winter 2022
## Last Edit: B^2 1/21/2022
## Notes: O(n^2) completion
#############################

import time
import turtle

X_BOUND = 27
Y_BOUND = 27
STACK_SIZE = 1000


def main():
    # run one trial, see result
    run_trial(STACK_SIZE)


def show_results(board):
    sc = turtle.Screen()
    pen = turtle.Turtle()
    sc.setup(1000, 1000)
    pen.speed(0)
    for i in range(X_BOUND):
        pen.up()
        pen.setpos(-475, -400 + 30 * i)
        pen.down()
        for j in range(Y_BOUND):
            if board[j][i] == 0:
                col = 'white'
            elif board[j][i] == 1:
                col = 'yellow'
            elif board[j][i] == 2:
                col = 'orange'
            else:
                col = 'red'
            pen.fillcolor(col)
            pen.begin_fill()
            for _ in range(4):
                pen.forward(30)
                pen.left(90)
            pen.forward(30)
            pen.end_fill()
    turtle.exitonclick()


def run_trial(chip_stack_size=120):
    # make board and set starting point
    board = [[0 for _ in range(X_BOUND)] for _ in range(Y_BOUND)]
    board[X_BOUND // 2][Y_BOUND // 2] = chip_stack_size

    # all points that have at least 4 chips
    geq_four_chips = set()
    geq_four_chips.add((X_BOUND // 2, Y_BOUND // 2))

    # BFS flood fill algorithm
    while len(geq_four_chips) > 0:
        try:
            location = geq_four_chips.pop()
            x_coord = location[0]
            y_coord = location[1]

            # check if curr has more than 4
            if board[y_coord][x_coord] >= 4:
                board[y_coord][x_coord] -= 4
                if board[y_coord][x_coord] >= 4:
                    geq_four_chips.add((x_coord, y_coord))

                # spread 1 chip to each neighbor
                right = x_coord + 1
                if 0 <= right < X_BOUND:
                    board[y_coord][right] += 1
                    geq_four_chips.add((right, y_coord))

                left = x_coord - 1
                if 0 <= left < X_BOUND:
                    board[y_coord][left] += 1
                    geq_four_chips.add((left, y_coord))

                up = y_coord + 1
                if 0 <= up < Y_BOUND:
                    board[up][x_coord] += 1
                    geq_four_chips.add((x_coord, up))

                down = y_coord - 1
                if 0 <= down < Y_BOUND:
                    board[down][x_coord] += 1
                    geq_four_chips.add((x_coord, down))

        except KeyError:
            break

    show_results(board)
    #print_board(board)


def print_board(board):
    # formats the board
    board_copy = board
    for x in range(X_BOUND):
        for y in range(Y_BOUND):
            if board[y][x] == 0:
                board[y][x] = ""
    # prints the board
    for line in board_copy:
        print(line)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/