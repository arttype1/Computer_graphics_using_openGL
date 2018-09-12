# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
#Example 2.2.2 Drawing the Sierpinski gasket
import sys
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from copy import copy
import time
import random as rd
class GLintPoint:
    def __init__(self, x, y):
        assert isinstance(x, int)
        self.x = x
        assert isinstance(y, int)
        self.y = y

def myInit():
    glClearColor(0.0,0.0,0.0,0.0)
    glColor3f(1.0,1.0,1.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 1280.0, 0.0, 960.0)

def Sierpinski():
    glClear(GL_COLOR_BUFFER_BIT)
    T = [GLintPoint(1,1), GLintPoint(1200,1), GLintPoint(600,960)]
    index =  rd.randint(0, 2)
    point = copy(T[index])
    glBegin(GL_POINTS)
    glVertex2f(point.x,point.y)
    for i in range(100000):
        index = rd.randint(0, 2)
        glColor3f(point.x/1200, point.y/960, 1.0)
        point.x = (point.x + T[index].x) / 2
        point.y = (point.y + T[index].y) / 2
        glVertex2f(point.x,point.y)
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1280,960)
    glutInitWindowPosition(100,150)
    glutCreateWindow(b"the Sierpinski gasket")

#register the callback functions
    glutDisplayFunc(Sierpinski)
#    glutReshapeFunc(myReshape)
#    glutMouseFunc(myMouse)
#    glutKeyboardFunc(myKeyboard)

    myInit()
    glutMainLoop()

main()