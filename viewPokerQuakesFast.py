#############################
## Written by Benjamen Gao
## For Math 101 Winter 2022
## Last Edit: B^2 2/4/2022
## Notes: Donne
#############################

import time
from graphics import Canvas

SHIFT = 40
X_BOUND = 40 #450
Y_BOUND = 40 #50
STACK_SIZE = 729 #314159


def main():
    t0 = time.time()
    # run one trial, see result
    board = run_trial(STACK_SIZE)
    canvas = create_canvas()
    draw_grid_canvas(board, canvas)
    t1 = time.time()
    print(t1 - t0)
    canvas.mainloop()


def create_canvas():
    return Canvas(X_BOUND * 40, Y_BOUND * 40, f'Steady State Configuration Starting Stack Size of {STACK_SIZE} Chips')


def draw_grid_canvas(grid, canvas, scale=10):
    """
    Draw grid to tk canvas, erasing and then filling it.
    This was ultimately the best performing approach.
    scale is pixels per block
    """
    # pixel size of canvas
    grid_length = len(grid)

    # draw black per spot
    for y in range(grid_length):
        for x in range(grid_length):
            val = grid[y][x]
            if val == 0:
                color = 'white'
            elif val == 1:
                color = 'yellow'
            elif val == 2:
                color = 'orange'
            else:
                color = 'red'
            canvas.create_rectangle((1 + x * scale) + SHIFT, (1 + y * scale) + SHIFT, (1 + x * scale) + scale + SHIFT,
                                    (1 + y * scale) + scale + SHIFT, fill=color, outline=color)
    canvas.update()


def run_trial(chip_stack_size):
    # make board and set starting point
    board = [[0 for _ in range(X_BOUND)] for _ in range(Y_BOUND)]
    board[X_BOUND // 2][Y_BOUND // 2] = chip_stack_size

    # all points that have at least 4 chips
    geq_four_chips = set()
    geq_four_chips.add((X_BOUND // 2, Y_BOUND // 2))

    # BFS flood fill algorithm
    while geq_four_chips:
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
                board[y_coord][right] += 1
                geq_four_chips.add((right, y_coord))

                left = x_coord - 1
                board[y_coord][left] += 1
                geq_four_chips.add((left, y_coord))

                up = y_coord + 1
                board[up][x_coord] += 1
                geq_four_chips.add((x_coord, up))

                down = y_coord - 1
                board[down][x_coord] += 1
                geq_four_chips.add((x_coord, down))

        except KeyError:
            break

    return board


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
