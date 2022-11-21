import pygame as pg
import random
import threading
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


r1 = random.random()
g1 = random.random()
b1 = random.random()

r2 = random.random()
g2 = random.random()
b2 = random.random()

r3 = random.random()
g3 = random.random()
b3 = random.random()

rt = random.random()
gt = random.random()
bt = random.random()

rs = random.random()
gs = random.random()
bs = random.random()


def lab2():
    edges = ((0, 1), (0, 5), (0, 3),
             (0, 1), (0, 7), (0, 3),

             (0, 2), (0, 5), (0, 4),
             (0, 2), (0, 8), (0, 4),

             (0, 3), (0, 8), (0, 2),
             (0, 3), (0, 6), (0, 2),

             (0, 4), (0, 6), (0, 1),
             (0, 4), (0, 7), (0, 1),
             )

    lines = (
        (0, 1), (1, 7), (1, 6), (0, 6),
        (0, 5), (0, 3), (3, 5), (0, 7),
        (0, 2), (0, 8), (2, 8), (2, 6),
        (0, 4), (4, 5), (4, 8), (7, 3),
    )

    def PyramidLines(height, width, edges, color):
        vertices = ((0.0, 2.5 + height, 0.0),
                    # outer
                    (1.0 + width, 1.0 + height, -1.0 - width),
                    (-1.0 - width, 1.0 + height, -1.0 - width),
                    (1.0 + width, 1.0 + height, 1.0 + width),
                    (-1.0 - width, 1.0 + height, 1.0 + width),
                    # inner
                    (0.0, 1.0 + height, 0.5),
                    (0.0, 1.0 + height, -0.5),
                    (0.5, 1.0 + height, 0.0),
                    (-0.5, 1.0 + height, 0.0))

        glBegin(GL_LINES)
        glColor4f(*color)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()

    def Pyramid(height, width, edges, color):
        vertices = (
            (0.0, 2.5 + height, 0.0),
            # outer
            (1.0 + width, 1.0 + height, -1.0 - width),
            (-1.0 - width, 1.0 + height, -1.0 - width),
            (1.0 + width, 1.0 + height, 1.0 + width),
            (-1.0 - width, 1.0 + height, 1.0 + width),
            # inner
            (0.0, 1.0 + height, 0.5),
            (0.0, 1.0 + height, -0.5),
            (0.5, 1.0 + height, 0.0),
            (-0.5, 1.0 + height, 0.0)
        )

        glBegin(GL_TRIANGLES)
        glColor4f(*color)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()

    def Trunk(color):
        glBegin(GL_TRIANGLES)
        glColor4f(*color)

        ACDB = (
            (0.2, -0.2),  # 10
            (0.27, 0),
            (0.2, 0.2),  # 11
            (0, 0.27),
            (-0.2, 0.2),  # 01
            (-0.27, 0),
            (-0.2, -0.2),  # 00
            (0, -0.27),
            (0.2, -0.2),  # 10
        )
        for i in range(len(ACDB) - 1):
            glVertex3fv((ACDB[i][0], 0, ACDB[i][1]))
            glVertex3fv((ACDB[i + 1][0], 0, ACDB[i + 1][1]))
            glVertex3fv((ACDB[i + 1][0], -1, ACDB[i + 1][1]))

            glVertex3fv((ACDB[i][0], 0, ACDB[i][1]))
            glVertex3fv((ACDB[i][0], -1, ACDB[i][1]))
            glVertex3fv((ACDB[i + 1][0], -1, ACDB[i + 1][1]))
        glEnd()

    def Top(top, color):
        glBegin(GL_TRIANGLES)
        glColor4f(*color)
        # base
        glVertex3fv((0.14, top, 0.14))
        glVertex3fv((-0.14, top, 0.14))
        glVertex3fv((0.14, top, -0.14))

        glVertex3fv((-0.14, top, -0.14))
        glVertex3fv((-0.14, top, 0.14))
        glVertex3fv((0.14, top, -0.14))

        edges = (
            (0.14, 0.14),
            (-0.14, 0.14),
            (-0.14, -0.14),
            (0.14, -0.14),
            (0.14, 0.14),
        )
        for i in range(len(edges) - 1):
            glVertex3fv((edges[i][0], top, edges[i][1]))
            glVertex3fv((edges[i + 1][0], top, edges[i + 1][1]))
            glVertex3fv((0, 0.5 + top, 0))
        glEnd()

    def TreeCubeToy(coords, color):
        glBegin(GL_TRIANGLES)
        glColor4f(*color)
        # base
        glVertex3fv((0.1 + coords[0], coords[1], 0.1 + coords[2]))
        glVertex3fv((-0.1 + coords[0], coords[1], 0.1 + coords[2]))
        glVertex3fv((0.1 + coords[0], coords[1], -0.1 + coords[2]))

        glVertex3fv((-0.1 + coords[0], coords[1], -0.1 + coords[2]))
        glVertex3fv((-0.1 + coords[0], coords[1], 0.1 + coords[2]))
        glVertex3fv((0.1 + coords[0], coords[1], -0.1 + coords[2]))

        glVertex3fv((0.1 + coords[0], 0.15 + coords[1], 0.1 + coords[2]))
        glVertex3fv((-0.1 + coords[0], 0.15 + coords[1], 0.1 + coords[2]))
        glVertex3fv((0.1 + coords[0], 0.15 + coords[1], -0.1 + coords[2]))

        glVertex3fv((-0.1 + coords[0], 0.15 + coords[1], -0.1 + coords[2]))
        glVertex3fv((-0.1 + coords[0], 0.15 + coords[1], 0.1 + coords[2]))
        glVertex3fv((0.1 + coords[0], 0.15 + coords[1], -0.1 + coords[2]))

        edges = ((0.1, 0.1),
                 (-0.1, 0.1),
                 (-0.1, -0.1),
                 (0.1, -0.1),
                 (0.1, 0.1),
                 )
        for i in range(len(edges) - 1):
            glVertex3fv((edges[i][0] + coords[0], coords[1], edges[i][1] + coords[2]))
            glVertex3fv((edges[i + 1][0] + coords[0], coords[1], edges[i + 1][1] + coords[2]))
            glVertex3fv((edges[i + 1][0] + coords[0], 0.2 + coords[1], edges[i + 1][1] + coords[2]))

            glVertex3fv((edges[i][0] + coords[0], coords[1], edges[i][1] + coords[2]))
            glVertex3fv((edges[i][0] + coords[0], 0.2 + coords[1], edges[i][1] + coords[2]))
            glVertex3fv((edges[i + 1][0] + coords[0], 0.2 + coords[1], edges[i + 1][1] + coords[2]))

        glEnd()

    def display():
        pg.init()
        display = (800, 600)
        pg.display.set_mode(display, DOUBLEBUF | OPENGL)

        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glEnable(GL_LIGHT0)
        gluPerspective(50, (display[0] / display[1]), 0.1, 50.0)

        glTranslatef(0.0, -1.0, -10)
        glRotatef(30, 10, 0, 0)

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
            glRotatef(1, 0, 1, 0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            Pyramid(1, -0.2, edges, (r1, g1, b1, 1.0))
            PyramidLines(1, -0.2, lines, (r1, g1, b1, 1.0))
            Pyramid(0, 0.0, edges, (r2, g2, b2, 1.0))
            PyramidLines(0, 0.0, lines, (r2, g2, b2, 1.0))
            Pyramid(-1, 0.2, edges, (r3, g3, b3, 1.0))
            PyramidLines(-1, 0.2, lines, (r3, g3, b3, 1.0))
            Trunk((rt, gt, bt, 1.0))
            Top(3.3, (rs, gs, bs, 1.0))
            Top(3.6, (rs, gs, bs, 1.0))

            TreeCubeToy((-1.1, -0.15, -1.1), (1.0, 0.16, 0.16, 1.0))
            TreeCubeToy((-1.1, -0.15, 1.1), (1.0, 0.98, 0.16, 1.0))
            TreeCubeToy((1.1, -0.15, -1.1), (1.0, 0.98, 0.16, 1.0))
            TreeCubeToy((1.1, -0.15, 1.1), (1.0, 0.16, 0.16, 1.0))

            TreeCubeToy((-1.0, 0.85, -1.0), (0.16, 0.16, 1.0, 1.0))
            TreeCubeToy((-1.0, 0.85, 1.0), (1.0, 0.16, 0.16, 1.0))
            TreeCubeToy((1.0, 0.85, -1.0), (1.0, 0.16, 0.16, 1.0))
            TreeCubeToy((1.0, 0.85, 1.0), (0.16, 0.16, 1.0, 1.0))

            TreeCubeToy((-0.8, 1.85, -0.8), (0.16, 0.8, 0.5, 1.0))
            TreeCubeToy((-0.8, 1.85, 0.8), (0.16, 0.16, 1.0, 1.0))
            TreeCubeToy((0.8, 1.85, -0.8), (0.16, 0.16, 1.0, 1.0))
            TreeCubeToy((0.8, 1.85, 0.8), (0.16, 0.8, 0.5, 1.0))

            pg.display.flip()
            pg.time.wait(10)

    display()


if __name__ == '__main__':
    lab2()
