# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
# Case Study 2.1 Pseudorandom clouds of dots
import sys
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random as rd
screenWidth = 1280
screenHeight = 960


def myInit():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, screenWidth, 0.0, screenHeight)


def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_LINES)
    for i in range(90000):
        r = rd.randint(0, 256) / 256
        g = rd.randint(0, 256) / 256
        b = rd.randint(0, 256) / 256
        glColor3f(r, g, b)
        x =rd.randint(0, screenWidth-30)
        y = rd.randint(0, screenHeight)
        glVertex2i(x, y)
        glVertex2i(x+30, y)

    glEnd()
    glFlush()




def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(screenWidth, screenHeight)
    glutInitWindowPosition(100, 150)
    glutCreateWindow(b'Pseudorandom clouds of dots')

    # register the callback functions
    glutDisplayFunc(myDisplay)
    #    glutReshapeFunc(myReshape)
    #    glutMouseFunc(myMouse)
    #    glutKeyboardFunc(myKeyboard)
    #    glutMotionFunc(myMove)

    myInit()
    glutMainLoop()


main()
