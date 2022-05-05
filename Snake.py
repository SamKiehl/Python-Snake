import time, random, os

points = []
        
ICONS = {
    'n': '^',
    'e': '>',
    's': 'v',
    'w': '<'
}

BUTTONS = {
    'w': 'n',
    'd': 'e',
    's': 's',
    'a': 'w'
}

IN_FRONT = {
    'n': (-1, 0),
    'e': (0, 1),
    's': (1, 0),
    'w': (0, -1)
}

maze = [
    ['#','#','#','#','#','#','#','#','#','#','#','#',],
    ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',],
    ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',],
    ['#',' ',' ','>',' ',' ',' ',' ',' ',' ',' ','#',],
    ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',],
    ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',],
    ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',],
    ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',],
    ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',],
    ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',],
    ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',],
    ['#','#','#','#','#','#','#','#','#','#','#','#',],
]

START = (3, 3)
coords = START
facing = 'e'
points.append(START)

def p(maze): # Prints the maze.
    os.system('CLS')
    for r in maze:
        row = ''
        for c in r:
            row += f'{c} '
        print(row)

def in_front() -> str:
    return maze[coords[0] + IN_FRONT[facing][0]][coords[1] + IN_FRONT[facing][1]]

def update_points():
    global maze, points
    for i in range(1, len(points)):
        maze[points[i][0]][points[i][1]] = 's'

def turn(dir): # Turns the (character?)
    global maze, facing, coords
    if (((dir == '')) or (facing == 'n' and BUTTONS[dir] == 's') or (facing == 'e' and BUTTONS[dir] == 'w') or (facing == 's' and BUTTONS[dir] == 'n') or (facing == 'w' and BUTTONS[dir] == 'e')):
        return
    facing = BUTTONS[dir]
    maze[coords[0]][coords[1]] = ICONS[facing]

def forward(): # Moves the (character?) forward depending on which direction it is facing.
    global maze, facing, coords, points
    maze[coords[0]][coords[1]] = ' '

    maze[points[len(points) - 1][0]][points[len(points) - 1][1]] = ' '
    for i in range(len(points) - 1, 0, -1):
        points[i] = points[i-1]

    coords = (coords[0] + IN_FRONT[facing][0], coords[1] + IN_FRONT[facing][1])
    maze[coords[0]][coords[1]] = ICONS[facing]
    points[0] = (coords[0], coords[1])

def iterate():
    global points, coords
    # p(maze)
    apple = False
    score = 0
    with(open('Controls.txt', 'r') as f):

        while(score < 98):

            # print(points)
            if not apple:
                r = coords[0]
                c = coords[1]
                while maze[r][c] != ' ':
                    r = random.randint(1, 10)
                    c = random.randint(1, 10)
                maze[r][c] = 'o'
                apple = True
            p(maze)

            inp = ''

            time.sleep(0.4)
            inp = f.read()[0::-1]
            # print(inp)
            turn(inp)

            p(maze)
            time.sleep(0.2)
            if(in_front() != 'o' and in_front() != ' '):
                break
            elif(in_front() == 'o'):
                score += 1
                apple = False
                points.insert(0, (coords[0] + IN_FRONT[facing][0], coords[1] + IN_FRONT[facing][1]))
                update_points()
                maze[coords[0] + IN_FRONT[facing][0]][coords[1] + IN_FRONT[facing][1]] = ICONS[facing]
                coords = [coords[0] + IN_FRONT[facing][0], coords[1] + IN_FRONT[facing][1]]
            else:
                forward()
                update_points()
                # print(points)
            p(maze)
        with(open('./Controls.txt', 'w') as d):    
            d.truncate(0)
            d.close()
        f.close()
    print(f'Game Over! Score: {score}')

if __name__ == '__main__':
    iterate()