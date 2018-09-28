# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
# Exercise 3_5_4 Drawing meanders

from Canvas import Canvas
from OpenGL.GLUT import *

cvs = Canvas(640, 480, 'Drawing meanders')


def meander(length, angle, space, num, thick):
    global cvs
    cvs.thick(thick)
    for i in range(num):
        cvs.forward(length, True)   # East
        cvs.turn(angle)
        cvs.forward(4 * space, True)  # North
        cvs.turn(angle)
        cvs.forward(4 * space, True)  # West
        cvs.turn(angle)
        cvs.forward(2 * space, True)  # South
        cvs.turn(-angle)
        cvs.forward(4 * space, True)  # West
        cvs.turn(-angle)
        cvs.forward((4 * space), True)  # North
        cvs.turn(-angle)
        cvs.forward(length, True)  # East
        cvs.turn(-angle)
        cvs.forward(length - (4 * space), True)  # South
        cvs.turn(angle)


def my_display():
    global cvs
    cvs.set_bc(1.0, 1.0, 1.0)
    cvs.clear_screen()
    cvs.set_color(0, 0, 0)
    cvs.cp = [10, 100]
    cvs.cd = 0
    meander(20, 90, 2,20,2)
    cvs.swap()




# register the callback functions
glutDisplayFunc(my_display)
glutMainLoop()
