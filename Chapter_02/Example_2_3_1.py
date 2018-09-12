# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
#Example 2.3.1 Drawing line graphs
import sys
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import tan

screenWidth = 640
screenHeight = 480
A = screenWidth / 4
B= screenWidth /2
C = screenHeight / 2


def myInit():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(2.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, screenWidth, 0.0, screenHeight)


def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINES)
    glVertex2f(0,C)
    glVertex2f(screenWidth,C)
    glVertex2f(A*2,0)
    glVertex2f(A*2,screenHeight)
    glEnd()
    glBegin(GL_LINE_STRIP)
    for i in range(210):
        x = i/10 - 10
        y = tan(x)
        glVertex2f((A/4*x)+B, (C/4*y)+C)
    glEnd()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1280, 960)
    glutInitWindowPosition(100, 150)
    glutCreateWindow(b"drawing line graphs")

    # register the callback functions
    glutDisplayFunc(myDisplay)
    #    glutReshapeFunc(myReshape)
    #    glutMouseFunc(myMouse)
    #    glutKeyboardFunc(myKeyboard)

    myInit()
    glutMainLoop()


main()
