import sys
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class Canvas:
    """
    cp 'center point' is a tuple (x,y)
    viewport and window are tuples (left, right, bottom, top)
    """
    def __init__(self, width, height, window_title: str):
        self.cp = (0, 0)
        self.viewport = (0, width, 0,  height)
        self.window = (0, width, 0,  height)
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowSize(width, height)
        glutInitWindowPosition(100, 150)
        glutCreateWindow(b'{window_title}')

    @property
    def window_aspect(self):  # width / height
        return (self.window[1] - self.window[0]) / (self.window[3] - self.window[2])

    def clear_screen(self):
        pass

    def set_bc(self, r, g, b):
        pass

    def set_color(self, r, g, b):
        pass

    def line_to(self, x, y):
         glBegin(GL_LINES)
         glVertex2f(self.cp[0], self.cp[y])
         glVertex2f(x, y)
         glEnd()
         glFlush()
         self.cp = (x, y)

    def move_to(self, x, y):
        self.cp = (x, y)
