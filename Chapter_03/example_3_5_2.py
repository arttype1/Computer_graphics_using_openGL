# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
# Example 3_5_2 a hook motif(Turtle Graphics)

from Canvas import Canvas
from OpenGL.GLUT import *

cvs = Canvas(640, 480, 'a hook motif(Turtle Graphics)')


def hook(side):
    global cvs
    cvs.forward(3 * side, True)
    cvs.turn(90)
    cvs.forward(side, True)
    cvs.turn(90)
    cvs.forward(side, True)
    cvs.turn(90)


def my_display():
    global cvs
    cvs.set_bc(1.0, 1.0, 1.0)
    cvs.clear_screen()
    cvs.set_color(0, 0, 0)
    cvs.cp = [250 , 350]
    for i in range(4):
        hook(70)


# register the callback functions
glutDisplayFunc(my_display)
glutMainLoop()
