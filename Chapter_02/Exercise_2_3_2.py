# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
#Exercise 2.3.1 Alternative ways to specify a rectangle
import sys
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class GLintPoint:
    def __init__(self, x, y):
        assert isinstance(x, int)
        self.x = x
        assert isinstance(y, int)
        self.y = y

screenWidth = 640
screenHeight = 640

def myInit():
    glClearColor(0.0,0.0,0.0,0.0)
    glColor3f(1.0,1.0,1.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, screenWidth, 0.0, screenHeight)

def drawRectangleCenter(centerpoint, width, height):
    glColor3f(0, 0, 1)
    glRectf(centerpoint.x-width/2, centerpoint.y-height/2, centerpoint.x+width/2, centerpoint.y+height/2)

def drawRectangleCornerSize(corner, width, ratio):
    glColor3f(1, 0, 0)
    glRectf(corner.x, corner.y - width/ratio, corner.x+width, corner.y)

def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    drawRectangleCenter(GLintPoint(50,250), 50, 400)
    drawRectangleCornerSize(GLintPoint(250, 250), 150, 1.618034)
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(screenWidth, screenHeight)
    glutInitWindowPosition(100,150)
    glutCreateWindow(b"Alternative ways to specify a rectangle")

#register the callback functions
    glutDisplayFunc(myDisplay)
#    glutReshapeFunc(myReshape)
#    glutMouseFunc(myMouse)
#    glutKeyboardFunc(myKeyboard)

    myInit()
    glutMainLoop()

main()
