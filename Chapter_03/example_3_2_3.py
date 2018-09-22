# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
# Example 3_2_3 Tiling the screen window
import sys
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
# globals
screenWidth = 640
screenHeight = 440
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
    glColor3f(0.0, 0.0, 0.0)
    for i in range(10):
        for j in range(10):
            if (i + j) %2 == 0:
                setWindow(0, 640.0, 0, 440.0)
            else:
                setWindow(0, 640.0, 440.0, 0)
            glViewport(i * 64, j * 44, 64, 44)
            f = open("dino.dat")
            numpolys = f.readline()
            num = int(numpolys)
            for p in range(num):
                numLines = f.readline()
                lines = int(numLines)
                glBegin(GL_LINE_STRIP)
                for q in range(lines):
                    xy = f.readline()
                    x = int(xy.split(" ")[0])
                    y = int(xy.split(" ")[1])
                    glVertex2i(x, y)
                glEnd()
            f.close()
        glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(screenWidth, screenHeight)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b'Tiling the screen window')

    # register the callback functions
    glutDisplayFunc(myDisplay)
    #    glutReshapeFunc(myReshape)
    #    glutMouseFunc(myMouse)
    #    glutKeyboardFunc(myKeyboard)
    #    glutMotionFunc(myMove)
    glutMainLoop()


main()