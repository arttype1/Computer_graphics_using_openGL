# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
# Case Study 2.2 Polyline editor
# ver0.02 can now select a point on the polyline with left mouse button and move it.
# ver0.01 reads points from a txt file and stores them in a'polyline' and draws the polyline
#################################################################################################
import sys
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import sqrt

screenWidth = 640
screenHeight = 480
polyline = []
poly_index = -1

def distance(x1, y1, x2, y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def myInit():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(8.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, screenWidth, 0.0, screenHeight)

def myMouse(button, state, x, y):
    global poly_index
    global polyline
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        dist_list= []
        for item in polyline:
            dist_list.append(distance(x, screenHeight - y,item[0],item[1]))
            if not len(dist_list) == 0:
                poly_index = dist_list.index(min(dist_list))
            else:
                poly_index = -1
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        poly_index = -1

def myMove(x, y):
    global poly_index
    global polyline
    polyline[poly_index] = (x, screenHeight - y)


def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1)
    global polyline
    global poly_index

    glBegin(GL_LINE_STRIP)
    for i in polyline:
        glVertex2i(i[0], i[1])
    glEnd()
    if not poly_index == -1:
        glBegin(GL_POINTS)
        glColor3f(0,1,0)
        glVertex2i(polyline[poly_index][0], polyline[poly_index][1])
        glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(screenWidth, screenHeight)
    glutInitWindowPosition(100, 50)
    glutCreateWindow(b'Polyline editor')

    # register the callback functions
    glutDisplayFunc(myDisplay)
    #    glutReshapeFunc(myReshape)
    glutMouseFunc(myMouse)
    #    glutKeyboardFunc(myKeyboard)
    glutMotionFunc(myMove)
    f = open('myfile.txt', 'r')
    poly_as_str = f.read()
    f.close()
    polys = poly_as_str.split()
    for i in polys:
        point_as_str = i.split(',')
        point_as_str[0] = point_as_str[0][1::]
        point_as_str[1] = point_as_str[1][0:-1:]
        point_as_int = (int(point_as_str[0]),int(point_as_str[1]))
        polyline.append(point_as_int)
    print(f'polyine = {polyline}')
    myInit()
    glutMainLoop()


main()
