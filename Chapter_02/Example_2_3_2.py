# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
#Example 2.3.2 Drawing polylines stored in a file
import sys
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

screenWidth = 640
screenHeight = 480

def myInit():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(2.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, screenWidth, 0.0, screenHeight)


def myDisplay():
    f = open("dino.dat")
    glClear(GL_COLOR_BUFFER_BIT)
    numpolys = f.readline()
    num = int(numpolys)
    for j in range(num):
        numLines = f.readline()
        lines = int (numLines)
        glBegin(GL_LINE_STRIP)
        for i in range(lines):
            xy = f.readline()
            x = int(xy.split(" ")[0])
            y = int(xy.split(" ")[1])
            glVertex2i(x,y)
        glEnd()
    glFlush()
    f.close()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1280, 960)
    glutInitWindowPosition(100, 150)
    glutCreateWindow(b"drawing polylines stored in a file")

    # register the callback functions
    glutDisplayFunc(myDisplay)
    #    glutReshapeFunc(myReshape)
    #    glutMouseFunc(myMouse)
    #    glutKeyboardFunc(myKeyboard)

    myInit()
    glutMainLoop()


main()
