# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
# Case Study 2.7 Building and running a maze
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
numRows = 21
numCols = 30
make_maze = True
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
    if row >= 1:
        nbors.append((col, row-1))
    if row < (numRows):
        nbors.append((col, row+1))
    if col >= 1:
        nbors.append((col-1, row))
    if col < numCols:
        nbors.append((col+1,row))
    return nbors


def has_all_walls(cell: tuple):
    row = cell[1]
    col = cell[0]
    print(f'row = {row}, col = {col}')
    if (walls[row][col][1] +walls[row][col][0] +walls[row -1][col][0] +walls[row][col-1][1]) == 4:
        return True
    else:
        return False


def move_lab():
    global lab_mouse
    global walls
    global make_maze
    global un_visited
    if make_maze:
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
                if lab_mouse[0] > mouse_goto[0]:
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
                    make_maze = False
    else:
        pass
    glutPostRedisplay()


def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)

# #####################Color the cells########################
    for j in range(numRows + 1):
        y = (j * 20)
        for i in range(numCols):
            if (i, j) in un_visited:
                glColor3f(0, 1, 0)
                glRecti(i * 20 + 2, y + 2, i * 20 + 18, y + 18)
# #####################Color the walls########################
    glLineWidth(4)
    global walls
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    for j in range(numRows+1):
        # y = screenHeight - (j  * 20)
        y = (j * 20)
        for i in range(numCols+1):
            if walls[j][i][1] == 1:
                glVertex2i(i * 20 + 19, y)
                glVertex2i(i * 20 + 19, y + 20)
            if walls[j][i][0] == 1:
                glVertex2i(i * 20, y + 20)
                glVertex2i(i * 20 + 19, y + 20)
    glEnd()
# #####################Draw the mouse########################
    glColor3f(1, 0, 0)
    glEnable(GL_POINT_SMOOTH)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glPointSize(14)
    glBegin(GL_POINTS)
    glVertex2i(lab_mouse[0]*20 + 9, (lab_mouse[1]*20 +10))
    glEnd()
# #####################mEnd of drawing########################
    glFlush()
    if make_maze:
        move_lab()


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