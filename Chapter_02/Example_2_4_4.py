# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
#Example 2.4.4 Create a polyline using the mouse
import sys
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
screenWidth = 640
screenHeight = 640

class GLintPoint:
    def __init__(self, x, y):
        assert isinstance(x, int)
        self.x = x
        assert isinstance(y, int)
        self.y = y

my_polyline = []

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


def myMouse(button, state, x, y):
    global my_polyline
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        glClear(GL_COLOR_BUFFER_BIT)
        my_polyline.append((x,screenHeight - y))
        if len(my_polyline) > 1:
            glBegin(GL_LINE_STRIP)
            for i in range(len(my_polyline)):
                glVertex2i(my_polyline[i][0],my_polyline[i][1])
            glEnd()
            glFlush()
        else:
            glBegin(GL_POINTS)
            glVertex(x, screenHeight - y)
            glEnd()
            glFlush()
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        my_polyline = []    #reset the list
        glClear(GL_COLOR_BUFFER_BIT)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(screenWidth, screenHeight)
    glutInitWindowPosition(100, 150)
    glutCreateWindow(b"Create a polyline using the mouse")

    # register the callback functions
    glutDisplayFunc(myDisplay)
    #    glutReshapeFunc(myReshape)
    glutMouseFunc(myMouse)
    #    glutKeyboardFunc(myKeyboard)

    myInit()
    glClear(GL_COLOR_BUFFER_BIT)
    glutMainLoop()


main()
