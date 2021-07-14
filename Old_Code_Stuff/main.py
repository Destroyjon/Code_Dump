import pygame
import random
import time
from mover import mover
from Old_Code_Stuff.jsLib import Vector, mean


WIDTH, HEIGHT = 700, 700
midX, midY = WIDTH / 2, HEIGHT / 2
WHITE = (255, 255, 255)
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))


def population(count: int):
    mover_pop = []
    for i in range(count):
        i = mover(random.randint(0, WIDTH), 250, 0, random.uniform(0.01, 1))
        mover_pop.append(i)
    return mover_pop


gravity = Vector(0, 1)
wind = Vector()

movers = population(1000)


def draw_window():
    global db_time
    db_time = []
    start_time = time.time()

    DISPLAY.fill(WHITE, None, 5)
    global wind
    global gravity

    if pygame.mouse.get_pressed(3) == (1, 0, 0):
        # wind = Vector(0.01, -0.1)
        gravity = Vector()
    else:
        wind = Vector()
        gravity = Vector(0, 1)

    for i in range(len(movers)):
        weight = gravity * movers[i].mass
        movers[i].collision(movers)
        movers[i].applyforce(weight)
        movers[i].applyforce(wind)
        movers[i].friction(HEIGHT)
        # p3 = multiprocessing.Process(target=movers[i].collision(movers))
        movers[i].edges()
        movers[i].show(DISPLAY, (175, 20, 50))
        movers[i].update()

    pygame.display.update()

    db_time.append(round(time.time() - start_time, 3))


def main_loop():
    clock = pygame.time.Clock()
    run = True
    while run:
        # clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # js.Vector.set(walker1.pos, random.randint(0, 600), 200)
        draw_window()

    print(mean(db_time), 'Seconds')
    pygame.quit()


main_loop()
