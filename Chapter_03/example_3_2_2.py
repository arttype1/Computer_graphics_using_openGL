# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
# Example 3_2_2 Plotting the sinc function, revisited
import sys
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
# globals
screenWidth = 640
screenHeight = 480
# end globals


def setWindow(left, right, bottom, top):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(left, right, bottom, top)


def setViewport(left, right, bottom, top):
    glViewport(left, bottom, right - left, top -bottom)


def myDisplay():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    setWindow(-5.0, 5.0, -0.3, 2.0) # set the window
    setViewport(0, 640, 0, 480)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINE_STRIP)
    for x in range(81):
        x = (x -  40) / 10
        if x != 0:
            glVertex2f(x, math.sin(x* math.pi) / (x * math.pi))
    glEnd()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(screenWidth, screenHeight)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b'Plotting the sinc function, revisited')

    # register the callback functions
    glutDisplayFunc(myDisplay)
    #    glutReshapeFunc(myReshape)
    #    glutMouseFunc(myMouse)
    #    glutKeyboardFunc(myKeyboard)
    #    glutMotionFunc(myMove)
    glutMainLoop()


main()