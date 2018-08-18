# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
#EX2.3.1 Drawing the checkerboard
import sys
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

screenWidth = 480
screenHeight = 480

def myInit():
    glClearColor(0.0,0.0,0.0,0.0)
    glColor3f(1.0,1.0,1.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, screenWidth, 0.0, screenHeight)

def checkerboard(size):
    for i in range(8):
        for j in range(8):
            if((i+j)%2):
                glColor3f(1, 1, 0)
            else:
                glColor3f(153/256, 76/256, 0)
            glRectf(0 +i*size,0+ j*size,size+ i*size, size +j*size)
    glFlush()

def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    checkerboard(screenHeight/8)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(screenWidth, screenHeight)
    glutInitWindowPosition(100,150)
    glutCreateWindow(b"Drawing the checkerboard")

#register the callback functions
    glutDisplayFunc(myDisplay)
#    glutReshapeFunc(myReshape)
#    glutMouseFunc(myMouse)
#    glutKeyboardFunc(myKeyboard)

    myInit()
    glutMainLoop()

main()