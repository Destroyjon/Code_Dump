import pygame
import random
from test_mover import mover
from Old_Code_Stuff.jsLib import Vector, mean
import time

# Initialize Window
MAIN_WIDTH = 700
MAIN_HEIGHT = 700
DISPLAY_WH = (MAIN_WIDTH, MAIN_HEIGHT)
MD_COLOR = (255, 255, 255)
global MAIN_WINDOW
MAIN_WINDOW = pygame.display.set_mode(DISPLAY_WH)
MAIN_WINDOW.fill(MD_COLOR)

pygame.display.set_caption('Multi-Proccessing')

pygame.display.init()
pygame.display.flip()


# Test how long code takes
# db_time = []
# start_time = time.time()
# end_time = db_time.append(time.time() - start_time)
# print(mean(db_time), 'Seconds')
# Test how long code takes

#Constant Forces
G = Vector(0, 1)
B = Vector(0, 0)
D = Vector(0, 0)
A = Vector(0, 0)
# Initialize Code
masses = [10, 100, 250, 1000]
#masses = [10]
def population(count: int):
    mover_pop = [mover(random.randint(0, MAIN_WIDTH), random.randint(0, MAIN_HEIGHT), 0, random.randint(1, 2), 20) for _ in range(count)]
    return mover_pop

movers = population(50)
movers = set(movers)

def calc_physics(m):
    m.applyForce(G, B, D, A)
    m.applyForce(Vector(0, 0))
    #m.airResistance(0.1)
    m.update()
    m.edges()
    m.detect_collision(movers)
    m.show(MAIN_WINDOW)

def draw_loop():
    global db_time
    db_time = []

    MAIN_WINDOW.fill(MD_COLOR)

    start_time = time.time()

    for m in movers:
        calc_physics(m)

    db_time.append(time.time() - start_time)

    pygame.display.update()

def main_loop():
    # Main Loop
    Clock = pygame.time.Clock()
    running = True
    while running:
        Clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_loop()

    print(round(mean(db_time), 4), 'Average Seconds To Complete')
    pygame.quit()

if __name__ == '__main__':
    main_loop()



def Chunk():

    self.chunkObjects = set(movers)

    def del_obj(object):
        chunkObjects.remove(object)

    def add_obj(object):
        chunkObjects.add(object)

    return chunkObjects