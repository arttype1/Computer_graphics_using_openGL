# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
# Exercise 3_8_5 Drawing a logo

from Canvas import Canvas
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import time

cvs = Canvas(1280, 960, 'Drawing a logo')


def curve(w,h,n,c):
    global cvs
    r,g,b = c
    cvs.set_color(r, g, b)
    glBegin(GL_POLYGON)
    for i in range(n+1):
        t = 2 * (math.pi * i) / n
        glVertex2f(w *math.cos(t), h * math.sin(t))
    glEnd()
    glFlush()


def my_display():
    global cvs
    cvs.set_bc(1, 1, 1)
    cvs.set_window(-4, 4, -4, 4)
    cvs.clear_screen()
    curve(3, 2, 42,(0,0,0))
    curve(1.9, 1.9, 42,(1,1,1))
    curve(1.85, 1.1, 42,(0,0,0))
    curve(1, 1, 42,(1,1,1))
    cvs.swap()


# register the callback functions
glutDisplayFunc(my_display)
glutMainLoop()
