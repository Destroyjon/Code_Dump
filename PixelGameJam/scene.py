import pygame
from ui_stuff import Button


class BattleScene(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.menu_buttons = pygame.sprite.Sprite()
        self.image = pygame.Surface([width, height])
        self.menu_buttons.image = pygame.Surface.subsurface(self.image, [0, 0, width, height-(height/3)])
        self.image.fill((75, 75, 75))
        self.menu_buttons.image.fill((150, 200, 150))
        self.rect = self.image.get_rect()
        self.menu_buttons.rect = self.menu_buttons.image.get_rect()
        self.background_group = pygame.sprite.Group(self, self.menu_buttons)
        button_top_l = Button(175, height-175, 300, 75, (125, 125, 150))
        button_top_r = Button(500, height-175, 300, 75, (150, 125, 125))
        button_bottom_l = Button(175, height-75, 300, 75, (125, 150, 125))
        button_bottom_r = Button(500, height-75, 300, 75, (150, 150, 125))
        small_button_top_l = Button(width-225, height-160, 125, 60, (125, 125, 150))
        small_button_top_r = Button(width-90, height-160, 125, 60, (150, 125, 125))
        small_button_bottom_l = Button(width-225, height-90, 125, 60, (125, 150, 125))
        small_button_bottom_r = Button(width-90, height-90, 125, 60, (150, 150, 125))
        self.button_group = pygame.sprite.Group(button_top_l, button_top_r, button_bottom_r, button_bottom_l)
        self.button_group.add(small_button_top_l, small_button_top_r, small_button_bottom_l, small_button_bottom_r)

    def draw(self, screen):
        self.background_group.draw(screen)
        self.button_group.draw(screen)

    def add_buttons(self, *buttons):
        self.button_group.add(*buttons)

    def update(self):
        self.button_group.update()


class MainMenu:
    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        self.screen.fill((200, 200, 233))
