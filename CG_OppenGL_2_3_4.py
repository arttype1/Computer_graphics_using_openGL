# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
#2.3.4 Building a polyline drawer
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

def drawPolyLine(poly, closed):
    if (closed):
        glBegin( GL_LINE_LOOP)
    else:
        glBegin(GL_LINE_STRIP)
    for i in range(len(poly)):
        glVertex2i(poly[i].x, poly[i].y)
    glEnd()
    glFlush()
def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    #store some random points in a list
    poly = [GLintPoint(0,0), GLintPoint(100,100), GLintPoint(200,100)]
    drawPolyLine(poly, 1)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1280,960)
    glutInitWindowPosition(100,150)
    glutCreateWindow(b"Building a polyline drawer")

#register the callback functions
    glutDisplayFunc(myDisplay)
#    glutReshapeFunc(myReshape)
#    glutMouseFunc(myMouse)
#    glutKeyboardFunc(myKeyboard)

    myInit()
    glutMainLoop()

main()