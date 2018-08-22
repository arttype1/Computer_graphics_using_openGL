# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
# 2.3.1 "Freehand" drawing with a fat brush
import sys
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
screenWidth = 640
screenHeight = 640


def myInit():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(4.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, screenWidth, 0.0, screenHeight)


def myDisplay():
    glColor3f(1, 1, 1)
    glFlush()


def myMove(x, y):
        brush_size = 20
        glRecti(x,screenHeight - y,x+brush_size,screenHeight - y + brush_size)
        glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(screenWidth, screenHeight)
    glutInitWindowPosition(100, 150)
    glutCreateWindow(b'"Freehand" drawing with a fat brush')

    # register the callback functions
    glutDisplayFunc(myDisplay)
    #    glutReshapeFunc(myReshape)
    #    glutMouseFunc(myMouse)
    #    glutKeyboardFunc(myKeyboard)
    glutMotionFunc(myMove)

    myInit()
    glClear(GL_COLOR_BUFFER_BIT)
    glutMainLoop()


main()
