#############################
## Written by Benjamen Gao
## For Math 101 Winter 2022
## Last Edit: B^2 1/14/2022
## Notes: Fixed Non-Moving
#############################

X_BOUND = 31
Y_BOUND = 31
NUM_TRIALS = 100
MAXIMAL_STACK = 1000


def main():
    # run many trials, see if they all have the same result
    all_same = True
    for stack_size in range(MAXIMAL_STACK):
        if stack_size % 100 == 0:
            print(f'at: {stack_size}')
        board_result = run_trial(stack_size)
        for _ in range(NUM_TRIALS):
            if board_result != run_trial(stack_size):
                all_same = False

    print(f"After {NUM_TRIALS} trials for each stack size from 0 to {stack_size}, all {NUM_TRIALS} trials for each"
          f"stack size are consistent!") if all_same else print("Inconsistent!")


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

    # if u wanna see the board uncomment the below
    # print_board(board)
    return make_str(board)


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


def make_str(board):
    # makes board into a str
    board_str = str()
    for line in board:
        for elem in line:
            board_str += str(elem)
    return board_str


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/