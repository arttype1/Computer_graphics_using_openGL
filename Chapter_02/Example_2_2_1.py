# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
#Example 2.2.1 The Big Dipper
import sys
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def myInit():
    glClearColor(0.0,0.0,0.0,0.0)   #black sky
    glColor3f(1.0,1.0,1.0)          #white stars
    glPointSize(4.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0,640.0,0.0,480.0)

def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    glVertex(289, 190)
    glVertex(320, 128)
    glVertex(239, 67)
    glVertex(194, 101)
    glVertex(129, 83)
    glVertex(75, 73)
    glVertex(74, 74)
    glVertex(20, 10)
    glEnd()
    glFlush()




def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640,480)
    glutInitWindowPosition(100,150)
    glutCreateWindow(b"The Big Dipper")

#register the callback functions
    glutDisplayFunc(myDisplay)
#    glutReshapeFunc(myReshape)
#    glutMouseFunc(myMouse)
#    glutKeyboardFunc(myKeyboard)

    myInit()
    glutMainLoop()

main()
