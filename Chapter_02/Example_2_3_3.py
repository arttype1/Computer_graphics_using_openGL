# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
#Example 2.3.3 Parameterizing figures
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
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, screenWidth, 0.0, screenHeight)


def parameterizedHouse(peak, width, height):
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINE_LOOP)  # draw the shell of house
    glVertex2f(peak[0], peak[1])
    glVertex2f(peak[0] + width / 2, peak[1] - (3 * height / 8))
    glVertex2f(peak[0] + width / 2, (peak[1]) - height)
    glVertex2f(peak[0] - width / 2, (peak[1]) - height)
    glVertex2f(peak[0] - width / 2, peak[1] - (3 * height / 8))
    glEnd()
    glBegin(GL_LINE_STRIP)  # draw the chimney
    glVertex2f(peak[0]- width / 3, peak[1]- height / 4)
    glVertex2f(peak[0]- width / 3, peak[1])
    glVertex2f(peak[0]- width / 6, peak[1])
    glVertex2f(peak[0]- width / 6, peak[1]- height / 8)
    glEnd()
    glBegin(GL_LINE_LOOP)  # draw the door
    glVertex2f(peak[0]- width / 3, peak[1]- height)
    glVertex2f(peak[0]- width / 12, peak[1]- height)
    glVertex2f(peak[0]- width / 12, (peak[1]- 9 * height / 16))
    glVertex2f(peak[0]- width / 3, (peak[1]- 9 * height / 16))
    glEnd()
    glBegin(GL_LINE_LOOP)  # draw the window
    glVertex2f(peak[0] + width / 12,(peak[1]-  5 * height /8))
    glVertex2f(peak[0] + width / 3,(peak[1]-  5 * height /8))
    glVertex2f(peak[0] + width / 3, peak[1]- height /2)
    glVertex2f(peak[0] + width / 12, peak[1]- height /2)
    glEnd()
    glFlush()


def myDisplay():
    parameterizedHouse([35, 60], 30, -40)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(screenWidth, screenHeight)
    glutInitWindowPosition(100, 150)
    glutCreateWindow(b"Parameterizing figures")

    # register the callback functions
    glutDisplayFunc(myDisplay)
    #    glutReshapeFunc(myReshape)
    #    glutMouseFunc(myMouse)
    #    glutKeyboardFunc(myKeyboard)

    myInit()
    glutMainLoop()


main()
