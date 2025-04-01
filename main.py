import random
import os
from pynput.keyboard import Key, Listener
from sty import fg, rs
import time
from intro import intro_screen, slow_print, game_over_text, gg

number_palette = {
    0: '    ',
    2: fg(255, 255, 0) + ' 02 ',
    4: fg(0, 255, 0) + ' 04 ',
    8: fg(0, 0, 255) + ' 08 ',
    16: fg(0, 128, 255) + ' 16 ',
    32: fg(255, 0, 255) + ' 32 ',
    64: fg(255, 0, 0) + ' 64 ',
    128: fg(255, 165, 0) + '0128',
    256: fg(128, 0 , 128) + '0256',
    512: fg(0, 128, 128) + '0512',
    1024: fg(255, 20, 147) + '1024',
    2048: fg(192, 192, 192) + '2048',
    4096: fg(128, 128 , 0) + '4096',
    8192: fg(0, 255, 255) + '8192'
}

grid_size = 0
grid = []
difficulty = 0

max_level = 0 # change according to level
game_won = False

safe_coords = []
key_pressed = '' # needed for pynput ONLY

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_board():
    global grid, grid_size, max_level

    grid_size = 5 if difficulty == 1 else 3 if difficulty == 4 else 4
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

    max_level = 2048 if difficulty < 3 else 4096 if difficulty == 3 else 8192

def difficulty_slider():
    global key_pressed, difficulty
    key_pressed = ''
    key = ''

    clear()

    print('Choose a difficulty twn 💔💔\n')
    print('1. Easy')
    print('2. Regular')
    print('3. Hard')
    print('4. Souls-like')
    print('5. Quit Game')

    while key not in ['1', '2', '3', '4', '5']:
        detect_keypress()

        try:
            key = key_pressed.char

        except:
            key = ''

    difficulty = int(key)

    print('\n\n')
    if key == '1':
        print('You lost all your aura with that.')

    elif key == '5':
        return True

    else:
        print('Loading your game.......')

    time.sleep(3)

    return False

def place_random_num():
    if len(safe_coords) != 0:
        coord = random.choice(safe_coords)
        safe_coords.remove(coord)
        grid[coord[0]][coord[1]] = 2

def detect_keypress():
    def the_name_of_this_function_does_not_matter(key):
        global key_pressed
        key_pressed = key
        return False

    with Listener(on_press=the_name_of_this_function_does_not_matter) as listener:
        listener.join()

def set_safe_coords() -> None:
    safe_coords.clear()

    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 0: safe_coords.append((i, j))

def print_grid(game_over):
    global score

    l = (2 * grid_size) + 7 
    k = (7 * grid_size) + 1

    window_len, window_height = os.get_terminal_size()

    vertical_padding = ((window_height - l)//2) - 4
    horizontal_padding = (window_len - k)//2 
    horizontal_pad = ' ' * (horizontal_padding - 1)

    for i in range(vertical_padding + 1):
        print(flush=True)

    print(horizontal_pad + '             Target', flush=True)
    print(horizontal_pad + f'              {max_level}' + '\n', flush=True)
    print(horizontal_pad + 'Press W, A, S or D to move around.', flush=True)
    print(horizontal_pad + 'Press G to exit the game.\n', flush=True)
    print(horizontal_pad, end = '', flush=True)
    print('=' * k, flush=True)

    for i in range(grid_size):
        print(horizontal_pad, end='', flush=True)
        print(end='| ', flush=True)

        for j in range(grid_size):
            print(end=f'{number_palette[grid[i][j]]}{rs.all} | ')

        print(f'\n', end=(horizontal_pad + '+' * k + '\n' if i != grid_size - 1 else ''), flush=True)

    print(horizontal_pad + '=' * k, flush=True)

    if game_over:
        clear()
        color = (255, 255, 0) if game_won else (255, 0, 0)
        message = gg if game_won else game_over_text
        delay = 5 if game_won else 3

        print(fg(*color))
        slow_print(message, delay)
        print(rs.all)

        time.sleep(3)

def rotate_anti():
    rotated_grid = []

    for i in range(grid_size - 1, -1, -1):
        rotated_row = []

        for j in range(grid_size):
            rotated_row.append(grid[j][i])

        rotated_grid.append(rotated_row)

    return rotated_grid

def rotate_clockwise():
    copy = []
    k = 0

    for i in range(grid_size):
        copy.append([])

        for j in range(grid_size - 1, -1, -1):
            copy[k].append(grid[j][i])

        k += 1

    return copy

def reflect():
    global grid
    reflected_grid = []

    for i in range(grid_size):
        reflected_row = []

        for j in range(grid_size - 1, -1, -1):
            reflected_row.append(grid[i][j])

        reflected_grid.append(reflected_row)
    return reflected_grid

def move_right():
    for i in range(grid_size):
        for j in range(grid_size - 2, -1, -1):
            if grid[i][j] == 0:
                continue

            k = j
            while k < grid_size - 1 and grid[i][k + 1] == 0:
                grid[i][k + 1] = grid[i][k]
                grid[i][k] = 0
                k += 1

            if k < grid_size - 1 and grid[i][k + 1] == grid[i][k]:
                grid[i][k + 1] *= 2
                grid[i][k] = 0

def move_left():
    global grid

    grid = reflect()
    move_right()
    grid = reflect()

def move_up():
    global grid

    grid = rotate_clockwise()
    move_right()
    grid = rotate_anti()

def move_down():
    global grid

    grid = rotate_anti()
    move_right()
    grid = rotate_clockwise()

def is_game_over():
    global game_won

    for row in grid:
        if max_level in row: 
            game_won = True
            return True

    if len(safe_coords) != 0: return False

    for i in range(grid_size):
        for j in range(grid_size - 1):
            if grid[i][j] == grid[i][j+1]: return False

    for i in range(grid_size - 1):
        for j in range(grid_size):
            if grid[i][j] == grid[i+1][j]: return False

    return True

def game_flow():
    clear()
    print(end='Please fullscreen before starting the game.\nPress any key to continue....')
    detect_keypress()

    intro_screen()
    detect_keypress()

    while True:
        if difficulty_slider():
            return 0
    
        generate_board()
        set_safe_coords()

        for _ in range(2):
            place_random_num()

        while True:
            clear()
            if is_game_over():
                print_grid(True)
                break

            print_grid(False)

            detect_keypress()
            try:
                key = key_pressed.char

            except:
                key = ''

            if key not in ['w', 'a', 's', 'd', 'g']:
                continue

            match key:
                case 'w': move_up()
                case 's': move_down()
                case 'a': move_left()
                case 'd': move_right()
                case 'g': break

            set_safe_coords()
            place_random_num()

game_flow()