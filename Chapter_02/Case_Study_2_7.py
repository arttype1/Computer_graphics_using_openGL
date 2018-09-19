# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
# Case Study 2.7 Building and running a maze
# veer0.0.4 runs the maze
# ver0.03 builds the maze
# ver0.02 added a lab_mouse that can break walls and move around
# ver0.01 draws the grid lines of the maze
#################################################################################################
import sys
from typing import List, Any

import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
import random


#SETUP
screenWidth = 640
screenHeight = 480
numRows = 42
numCols = 60
offset = int(screenWidth / (numCols +2))
inset  = 2
maze_mode = 'make'
goal = (0, 0)
un_visited: List[Any] =[]
lab_mouse = [random.randint(1, numCols-1), random.randint(1, numRows-1)]
walls = [[[1 for k in range(2)] for j in range(numCols+1)]for i in range(numRows+1)]
for c in range(numCols+1):
    walls[0][c][1] = 0
for r in range(numRows + 1):
    walls[r][0][0] = 0

def myInit():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, screenWidth, 0.0, screenHeight)


def find_nbors(row, col):
    nbors = []
    if row > 1:
        nbors.append((col, row-1))
    if row < (numRows):
        nbors.append((col, row+1))
    if col > 1:
        nbors.append((col-1, row))
    if col < numCols:
        nbors.append((col+1,row))
    return nbors


def has_all_walls(cell: tuple):
    row = cell[1]
    col = cell[0]
    if (walls[row][col][1] +walls[row][col][0] +walls[row -1][col][0] +walls[row][col-1][1]) == 4:
        return True
    else:
        return False


def has_no_wall(cell: tuple):
    global lab_mouse
    row = cell[1]
    col = cell[0]
    if lab_mouse[0] < cell[0]:
        # moving East
        if walls[lab_mouse[1]][lab_mouse[0]][1] == 0:
            return True
    elif lab_mouse[1] < cell[1]:
        # moving North
        if walls[lab_mouse[1]][lab_mouse[0]][0] == 0:
            return True
    elif lab_mouse[0] > cell[0]:
        # moving West
        if walls[cell[1]][cell[0]][1] == 0:
            return True
    elif lab_mouse[1] > cell[1]:
        # moving South
        if walls[cell[1]][cell[0]][0] == 0:
            return True
    else:
        return False


def solve_maze():
    pass
    global lab_mouse
    global walls
    global maze_mode
    global un_visited
    global goal
    if maze_mode == 'solve':
        nbors = find_nbors(lab_mouse[1], lab_mouse[0])
        if len(nbors) > 0:
            can_go = [item for item in nbors if has_no_wall(item)and item not in un_visited]
            if len(can_go) > 0:
                mouse_goto = can_go[random.randint(0, len(can_go) - 1)]
                if (lab_mouse[0], lab_mouse[1]) not in un_visited:
                    un_visited.append((lab_mouse[0], lab_mouse[1]))

            else:
                mouse_goto = un_visited.pop()
                if lab_mouse[0] < mouse_goto[0]:
                    # moving East
                    walls[lab_mouse[1]][lab_mouse[0]][1] = 1
                elif lab_mouse[1] < mouse_goto[1]:
                    # moving North
                    walls[lab_mouse[1]][lab_mouse[0]][0] = 1
                elif lab_mouse[0] > mouse_goto[0]:
                    # moving West
                    walls[mouse_goto[1]][mouse_goto[0]][1] = 1
                elif lab_mouse[1] > mouse_goto[1]:
                    # moving South
                    walls[mouse_goto[1]][mouse_goto[0]][0] = 1
            lab_mouse[0] = mouse_goto[0]
            lab_mouse[1] = mouse_goto[1]
            if lab_mouse[0] == goal[0] and lab_mouse[1] == goal[1]:
                maze_mode ='finished'
            glutPostRedisplay()


def make_maze():
    global lab_mouse
    global walls
    global maze_mode
    global un_visited
    global goal
    if maze_mode == 'make':
        nbors = find_nbors(lab_mouse[1], lab_mouse[0])
        if len(nbors) > 0:
            can_go =[item for item in nbors if has_all_walls(item)]
            if len(can_go) > 0:
                mouse_goto = can_go[random.randint(0,len(can_go)-1)]
                # for item in can_go:
                    # if item != mouse_goto:
                un_visited.append((lab_mouse[0], lab_mouse[1]))
                if lab_mouse[0] < mouse_goto[0]:
                    # moving East
                    walls[lab_mouse[1]][lab_mouse[0]][1] = 0
                elif lab_mouse[1] < mouse_goto[1]:
                    # moving North
                    walls[lab_mouse[1]][lab_mouse[0]][0] = 0
                elif lab_mouse[0] > mouse_goto[0]:
                    # moving West
                    walls[mouse_goto[1]][mouse_goto[0]][1] = 0
                elif lab_mouse[1] > mouse_goto[1]:
                    # moving South
                    walls[mouse_goto[1]][mouse_goto[0]][0] = 0
                lab_mouse[0] = mouse_goto[0]
                lab_mouse[1] = mouse_goto[1]
            else:
                if un_visited:
                    # jump the mouse
                    mouse_goto = un_visited.pop()
                    lab_mouse[0] = mouse_goto[0]
                    lab_mouse[1] = mouse_goto[1]
                else:
                    start = random.randint(2,numRows - 1)
                    end = random.randint(2,numRows - 1)
                    walls[start][0][1] = 0
                    lab_mouse[0] = 0
                    lab_mouse[1] = start
                    walls[end][numCols][1] = 0
                    maze_mode = 'solve'
                    goal = (numCols, end)
                    print(goal)
    glutPostRedisplay()



def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)

# #####################Color the cells########################
    for j in range(numRows + 1):
        y = (j * offset)
        for i in range(numCols + 1):
            x = (i * offset)
            if (i, j) in un_visited:
                glColor3f(0, 1, 0)
                glRecti(x + inset, y + inset, x + offset - inset, y + offset - inset)
# #####################Color the walls########################
    glLineWidth(4)
    global walls
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    for j in range(numRows+1):
        y = (j * offset)
        for i in range(numCols+1):
            x = (i * offset)
            if walls[j][i][1] == 1:
                glVertex2i(x + offset, y)
                glVertex2i(x + offset, y + offset)
            if walls[j][i][0] == 1:
                glVertex2i(x, y + offset)
                glVertex2i(x + offset, y + offset)
    glEnd()
# #####################Draw the mouse########################
    glColor3f(1, 0, 0)
    glEnable(GL_POINT_SMOOTH)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glPointSize(14)
    glBegin(GL_POINTS)
    glVertex2f(lab_mouse[0]*offset + offset/2, (lab_mouse[1]*offset + offset/2))
    glEnd()
# #####################mEnd of drawing########################
    glFlush()
    if maze_mode == 'make':
        make_maze()
    elif maze_mode == 'solve':
        solve_maze()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(screenWidth, screenHeight)
    glutInitWindowPosition(100, 50)
    glutCreateWindow(b'builging and running a maze')

    # register the callback functions
    glutDisplayFunc(myDisplay)
    #    glutReshapeFunc(myReshape)
    # glutMouseFunc(myMouse)
    # glutKeyboardFunc(myKeyboard)
    # glutMotionFunc(myMove)

    myInit()
    glutMainLoop()


main()