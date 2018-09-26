# Examples and Exercises From 'Computer Graphics using Open GL" by Hill 2nd Ed
# all code by George A. Merrill (except where otherwise noted)
#################################################################################################
# Example 3_5_1 An arrow marker

from Canvas import Canvas
from OpenGL.GLUT import *

cvs = Canvas(640, 480, 'An arrow marker')


def arrow(f, h, t, w):
    global cvs
    cvs.line_rel(-w - t/2, -f)
    cvs.line_rel(w, 0)
    cvs.line_rel(0, -h)
    cvs.line_rel(t, 0)
    cvs.line_rel(0, h)
    cvs.line_rel(w, 0)
    cvs.line_rel(-w - t/2, f)


def my_display():
    global cvs
    cvs.set_bc(1.0, 1.0, 1.0)
    cvs.clear_screen()
    cvs.set_color(0, 0, 0)
    cvs.cp = [250 , 350]
    arrow(150, 100, 70, 70)


# register the callback functions
glutDisplayFunc(my_display)
glutMainLoop()
