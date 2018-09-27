# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
# Exercise 3_5_7 Implementing Polyspiral

from Canvas import Canvas
from OpenGL.GLUT import *

cvs = Canvas(640, 480, 'Implementing Polyspiral')


def polyspiral(length, angle, incr, num):
    global cvs
    for i in range(num):
        cvs.forward(length, True)
        cvs.turn(angle)
        length += incr


def my_display():
    global cvs
    cvs.set_bc(1.0, 1.0, 1.0)
    cvs.clear_screen()
    cvs.set_color(1, 0, 0)
    cvs.cp = [170 , 350]
    cvs.cd = 0
    cvs.set_color(1, 0, 0)
    polyspiral(1,60, 1, 120)
    cvs.cp = [480 , 360]
    cvs.cd = 5
    cvs.set_color(0, 0, 1)
    polyspiral(1,89.5, 1, 190)
    cvs.cp = [150 , 100]
    cvs.cd = 0
    cvs.set_color(1, 1, 0)
    polyspiral(1, -144, 1, 170)
    cvs.cp = [480 , 130]
    cvs.cd = 0
    cvs.set_color(0, 0, 0)
    polyspiral(1, 170, 1, 250)


# register the callback functions
glutDisplayFunc(my_display)
glutMainLoop()
