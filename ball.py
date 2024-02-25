import pygame as pg
import math


class ball:
    def __init__(self, surface, pos, radius, length, color):
        self.surface = surface
        self.pos = [int(pos[0]), int(pos[1])]
        self.radius = int(radius)
        self.length = length
        self.color = color

    def draw(self):
        pg.draw.circle(self.surface, self.color, self.pos, self.radius)

    def move(self, omega, bvel, size):
        dt = 0.1
        gravity = 10
        ang = math.atan2((self.pos[1] - size[1]/2), (self.pos[0] - size[0]/2))
        alfa = (gravity / self.length) * math.sin(ang)
        omega += alfa * dt
        baccx = alfa * self.length * math.cos(ang) - omega**2 * self.length * math.sin(ang)
        baccy = alfa * self.length * math.sin(ang) + omega**2 * self.length * math.cos(ang)
        bacc = [baccx, baccy]
        bvel[0] += bacc[0] * dt
        bvel[1] += bacc[1] * dt
        self.pos[0] += int(bvel[0] * dt)
        self.pos[1] += int(bvel[1] * dt)
