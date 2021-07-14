import pygame
from random import uniform
from Old_Code_Stuff.jsLib import constrain, Vector
pygame.font.init()

class mover:
    def __init__(self, x=0, y=0, z=0, mass=1, radius=1):
        self.pos = Vector(x, y)
        self.vel = Vector(uniform(1, 1), uniform(1, 1))
        self.momentum = Vector()
        self.acc = Vector()
        self.mass = mass
        self.r = radius
        self.a = 3.14*self.r**2
        self.density = self.mass / self.a

    def __repr__(self):
        return 'Mover'

    def globalForce(func):
        def wrapper(self, *force):
            p = Vector()
            for f in force:
                p += f
            return func(self, p)
        return wrapper

    @globalForce
    def applyForce(self, force):
        force /= self.mass
        self.acc += force


    def friction(self, height):
        diff = height - (self.pos.y + self.r)
        if diff < 1:
            friction = self.vel
            friction = friction.normalize()
            friction *= -1
            mu = 0.1
            normal = self.mass
            friction = friction.setMag(mu * normal)


    def airResistance(self, p=1.22):
        CD = -0.41
        G = Vector(0, 0)
        weight = self.mass * G
        drag = self.vel * CD
        drag *= p
        #drag = drag * self.a
        force = weight + drag
        self.air = drag * 1


    def edges(self,width=700, height=700):
        vel = self.vel.normalize()
        vel = self.vel * -1
        if self.pos.y >= height-self.r:
            self.vel.y = vel.y
        if self.pos.y <= 0+self.r:
            self.vel.y = vel.y
        if self.pos.x >= width-self.r:
            self.vel.x = vel.x
        if self.pos.x <= 0+self.r:
            self.vel.x = vel.x

    def detect_collision(self, colliders):
        objects = set(colliders)
        objects.remove(self)
        for i in objects:
            distance = (((self.pos.x - i.pos.x) ** 2 + (self.pos.y - i.pos.y) ** 2)) ** 0.5

            if distance > (self.r + i.r):
                continue
            #elif distance <= (self.r + i.r) * 0.25:
                #self.vel = Vector.random2D() * 1
                #self.applyForce(self.collisionForce(i))
                #self.vel *= 1
                #self.acc = self.acc * 1
            elif distance <= (self.r + i.r)*0.95:
                self.vel = self.vel * 0.1
                self.applyForce(self.collisionForce(i))
                self.vel = self.vel * 0.5
                self.acc = self.acc * 5

    def collisionForce(self, object):
        u1 = self.vel
        u2 = object.vel
        new_v = self.pos - object.pos
        new_v = new_v.normalize()

        m1 = self.mass
        m2 = object.mass
        if m1 == m2:
            return new_v
        else:
            es1 = u1 * ((m1-m2)/(m1+m2))
            es2 = u2 * ((2*m2)/(m1+m2))
            v1 = es1 + es2
            return v1


    def setMass(self, mass):
        self.mass = mass
        return self.mass


    def update(self):
        dt = 0.75
        self.momentum = self.mass * self.vel
        self.momentum = Vector(abs(self.momentum.x), abs(self.momentum.y))
        self.vel += self.acc.limit(10)
        #mini = 0 * dt
        #if abs(self.acc.x) < mini and abs(self.acc.y) < mini:
        vel = Vector.copy(self.vel)
        self.pos = constrain((self.pos + vel), 0+self.r, 700-self.r)
        self.acc = Vector()
        



    def show(self, screen):
        contrast = 125
        color = (255/(200+self.mass)*contrast, 255/(230+self.mass)*contrast, 255/(200+self.mass)*contrast)
        #color_10 = (200/contrast, 255/contrast, 200/contrast)
        #color_100 = (150/contrast, 200/contrast, 150/contrast)
        #color_250 = (100/contrast, 150/contrast, 100/contrast)
        #color_500 = (50/contrast, 100/contrast, 50/contrast)
        #air = (self.pos.x - self.air.x, self.pos.y - self.air.y)
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = (round(abs(self.momentum.x + self.momentum.y), 1))
        text = self.mass

        #if self.mass <= 10:
        pygame.draw.circle(screen, color, (self.pos.x, self.pos.y), self.r)
            #pygame.draw.line(screen, color_10, (self.pos.x, self.pos.y), air)
        #textsurface = font.render('{}'.format(text), False, (0, 0, 0))
        #screen.blit(textsurface, (self.pos.x, self.pos.y))
        #elif self.mass <= 100:
            #pygame.draw.circle(screen, color, (self.pos.x, self.pos.y), self.r)
            #pygame.draw.line(screen, color_100, (self.pos.x, self.pos.y), air)
            #textsurface = font.render('{}'.format(text), False, (0, 0, 0))
            #screen.blit(textsurface, (self.pos.x, self.pos.y))
        #elif self.mass <= 250:
            #pygame.draw.circle(screen, color, (self.pos.x, self.pos.y), self.r)
            #pygame.draw.line(screen, color_250, (self.pos.x, self.pos.y), air)
            #textsurface = font.render('{}'.format(text), False, (0, 0, 0))
            #screen.blit(textsurface, (self.pos.x, self.pos.y))
        #else:
            #pygame.draw.circle(screen, color, (self.pos.x, self.pos.y), self.r)
            #pygame.draw.line(screen, color_500, (self.pos.x, self.pos.y), air)
            #textsurface = font.render('{}'.format(text), False, (0, 0, 0))
            #screen.blit(textsurface, (self.pos.x, self.pos.y))