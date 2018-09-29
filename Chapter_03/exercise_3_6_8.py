# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
# Exercise 3_6_8 Draw a pattern of stars

from Canvas import Canvas
from OpenGL.GLUT import *
import math
import time

cvs = Canvas(640, 480, 'Draw a pattern of stars')


def draw_star(size, center, color):
    global cvs
    cvs.set_color(color[0], color[1], color[2])
    cvs.cp = center
    cvs.cd = 90
    cvs.forward(size, False)
    cvs.cd = 108
    cvs.thick = int(size / 10)
    for i in range(5):
        cvs.turn(72 * 2)
        cvs.forward(1.902 * size)


def my_display():
    global cvs
    cvs.set_bc(0, 0, 0)
cvs.clear_screen()
rad_per_deg = 0.017453393
draw_star(100,[320, 240],(1, 1, 0))
for i in range(10):
    rj = rad_per_deg *i * 36
    x = 320 + (math.cos(rj) * 100)
    y = 240 + (math.sin(rj) * 100)
    draw_star(10, [x, y], (1, 0, 0))
    x = 320 + (math.cos(rj) * 200)
    y = 240 + (math.sin(rj) * 200)
    draw_star(30, [x, y], (0, 1, 0))
cvs.swap()



# register the callback functions
glutDisplayFunc(my_display)
glutMainLoop()
