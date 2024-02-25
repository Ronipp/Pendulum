import pygame as pg
import ball

pg.init()

white = (255, 255, 255)
black = (0, 0, 0)

size = [800, 600]
screen = pg.display.set_mode(size)
pg.display.set_caption('Pendulum')
clock = pg.time.Clock()

r = 20
len = 100
bpos = [size[0]/2, size[1]/2 + 200]
ball = ball.ball(screen, bpos, r, len, white)

done = False
while not done:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    ball.move(0, [0, 0], size)
    screen.fill(black)
    ball.draw()
    pg.display.flip()

pg.quit()
