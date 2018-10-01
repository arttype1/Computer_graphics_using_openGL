# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
# Exercise 3_6_12 A more elaborate figure

from Canvas import Canvas
from OpenGL.GLUT import *
import math
import time

cvs = Canvas(640, 480, 'A more elaborate figure')


def draw_hex(size, center, color):
    global cvs
    cvs.set_color(color[0], color[1], color[2])
    cvs.cp = center
    cvs.thick(2)
    for v in range(6):
        cvs.forward(size, True)
        cvs.turn(60)


def my_display():
    global cvs
    cvs.set_bc(1, 1, 1)
    cvs.clear_screen()
    cvs.cp = [320,240]
    cvs.cd = -60
    for i in range(15):
        draw_hex(90, [cvs.cp[0], cvs.cp[1]], (0, 0, 0))
        cvs.turn(360/15)
    cvs.swap()



# register the callback functions
glutDisplayFunc(my_display)
glutMainLoop()
