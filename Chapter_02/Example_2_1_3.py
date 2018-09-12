# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
#Example 2.1.3 Opening a window for Drawing
import sys
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def myInit():
    glClearColor(1.0,1.0,1.0,0.0)
    glColor3f(0.0,0.0,0.0)
    glPointSize(4.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0,640.0,0.0,480.0)

def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    glVertex(100, 50)
    glVertex(100, 130)
    glVertex(150, 130)
    glEnd()
    glFlush()




def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640,480)
    glutInitWindowPosition(100,150)
    glutCreateWindow(b"mywindow")

#register the callback functions
    glutDisplayFunc(myDisplay)
#    glutReshapeFunc(myReshape)
#    glutMouseFunc(myMouse)
#    glutKeyboardFunc(myKeyboard)

    myInit()
    glutMainLoop()

main()
