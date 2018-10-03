# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
# case_study_3_6 Tilings

from Canvas import Canvas
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import time
import random

cvs = Canvas(1280, 960, 'Tilings')
pict = 3

def curve(w,h, x, y, c):
    global cvs
    r,g,b = c
    cvs.set_color(r, g, b)
    glBegin(GL_LINE_STRIP)
    for i in range(41):
        t =  (math.pi * i) / 80
        glVertex2f(w *math.cos(t) + x, h * math.sin(t) + y)
    glEnd()
    glFlush()


def curve2(k, n, x, y, c):
    global cvs
    r,g,b = c
    cvs.set_color(r, g, b)
    glBegin(GL_LINE_STRIP)
    for i in range(41):
        t = math.pi * i/10
        f = k * t * n
        glVertex2f((f * math.cos(t)) + x, (f * math.sin(t)) + y)
    glEnd()
    glFlush()


def curve3(w,h, x, y, c):
    global cvs
    r,g,b = c
    cvs.set_color(r, g, b)
    glBegin(GL_LINE_STRIP)
    for i in range(41):
        t =  (math.pi * i) / 20
        glVertex2f(w *math.cos(t) + x, h * math.sin(t) + y)
    glEnd()
    glFlush()

def my_display():
    global cvs
    global pict
    cvs.set_bc(0, 0, 0)
    cvs.clear_screen()
    cvs.thick(2)
    if pict == 1:
        cvs.set_window(0, 4, 0, 4)
    elif pict == 2:
        cvs.set_window(-1, 1, -1, 1)
    elif pict == 3:
        cvs.set_window(-1, 1, -1, 1)
    for i in range(20):
        for j in range(15):
            cvs.set_viewport(64*i, 64*i + 64, 64*j, 64*j + 64)
            if pict == 1:
                curve(4, 4, 0, 0, (1,0,0))
                curve(-4, 4, 4, 0, (1,0,0))
                curve(-4, -4, 4, 4, (1,0,1))
                curve(4, -4, 0, 4, (1,0,1))
            elif pict == 2:
                curve2(.1, 1, 0, 0, (1, 1, 1))
                curve2(.1, -1, 0, 0, (1, 1, 1))
                curve2(.2, -1, 0, 0, (1, 1, 1))
                curve2(.2, 1, 0, 0, (1, 1, 1))
            elif pict == 3:
                cvs.set_window(-4, 4, -4, 4)
                tile = random.randint(0,1)
                if tile == 1:
                    curve3(4, 4, -4, -4, (1, 0, 0))
                    curve3(-4, 4, 4, 4, (0, 1, 0))
                else:
                    curve3(4, 4, -4, 4, (1, 1, 0))
                    curve3(-4, 4, +4, -4, (.6, .3, 0))

    cvs.swap()


# register the callback functions
glutDisplayFunc(my_display)
glutMainLoop()
