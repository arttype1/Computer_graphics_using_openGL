# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
# Example 3_2_6 Zooming in on a figure
import sys
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
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

    glColor3f(0.0, 0.0, 0.0)
    cx = 300.0
    cy = 200.0
    w = 12000
    asp = 0.7
    for frame in range(33):
        glClear(GL_COLOR_BUFFER_BIT)
        w *= 0.9
        h = w * asp
        setWindow(cx - w, cx + w, cy - h, cy+h)
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
        time.sleep(0.1)



def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(screenWidth, screenHeight)
    glutInitWindowPosition(100, 150)
    glutCreateWindow(b'Zooming in on a figure')

    # register the callback functions
    glutDisplayFunc(myDisplay)
    #    glutReshapeFunc(myReshape)
    #    glutMouseFunc(myMouse)
    #    glutKeyboardFunc(myKeyboard)
    #    glutMotionFunc(myMove)
    glutMainLoop()


main()