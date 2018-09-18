# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
# Case Study 2.7 Building and running a maze
# ver0.02 added a lab_mouse that can break walls and move around
# ver0.01 draws the grid lines of the maze
#################################################################################################
import sys
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

#SETUP
screenWidth = 640
screenHeight = 480
numRows = 21
numCols = 30
lab_mouse = [1, 9]
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


def move_lab():
    global lab_mouse
    global walls
    walls[lab_mouse[1]][lab_mouse[0]][1] = 0
    lab_mouse[0]+=1
    glutPostRedisplay()


def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 0)
    global walls
    glLineWidth(4)
    glBegin(GL_LINES)
    for j in range(numRows+1):
        y = screenHeight - ((j + 1) * 20)
        for i in range(numCols+1):
            if walls[j][i][1] == 1:
                glVertex2i((i) * 20 + 19, y)
                glVertex2i((i) * 20 + 19, y +20)
            if walls[j][i][0] == 1:
                glVertex2i((i) * 20, y)
                glVertex2i((i) * 20 + 19, y)
    glEnd()
    glColor3f(1, 0, 0)
    glEnable(GL_POINT_SMOOTH)
    glPointSize(8)
    glBegin(GL_POINTS)
    glVertex2i(lab_mouse[0]*20 + 10, screenHeight -(lab_mouse[1]*20 +10))
    glEnd()
    glFlush()
    if lab_mouse[0] < numCols:
        move_lab()
        time.sleep(0.1)


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