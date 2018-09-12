# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
#Example 2.4.2 Specifying a rectangle with the mouse
import sys
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
screenWidth = 640
screenHeight = 640
numCorners = 0
class GLintPoint:
    def __init__(self, x, y):
        assert isinstance(x, int)
        self.x = x
        assert isinstance(y, int)
        self.y = y

corner = [GLintPoint(0, 0), GLintPoint(0, 0)]

def myInit():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(4.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, screenWidth, 0.0, screenHeight)


def myDisplay():
    glColor3f(1, 0, 0)
    glFlush()


def myMouse(button, state, x, y):
    global numCorners
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        corner[numCorners]= GLintPoint(x, screenHeight - y)
        numCorners += 1
    if numCorners == 2:
        glRecti(corner[0].x, corner[0].y, corner[1].x, corner[1].y)
        numCorners = 0
        glFlush()
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        glClear(GL_COLOR_BUFFER_BIT)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(screenWidth, screenHeight)
    glutInitWindowPosition(100, 150)
    glutCreateWindow(b"Specifying a rectangle with the mouse")

    # register the callback functions
    glutDisplayFunc(myDisplay)
    #    glutReshapeFunc(myReshape)
    glutMouseFunc(myMouse)
    #    glutKeyboardFunc(myKeyboard)

    myInit()
    glClear(GL_COLOR_BUFFER_BIT)
    glutMainLoop()


main()
