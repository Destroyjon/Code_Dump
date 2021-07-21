import pygame
from player_class import Player


class Button:
    def __init__(self, screen, position, size=(100, 50), color=(0, 0, 0)):
        pygame.font.init()
        self.screen = screen
        self.position = position
        self.size = size
        self.color = color

    def set_button_size(self, size):
        self.size = size

    def get_button_size(self):
        return self.size

    def draw_button(self):
        pygame.draw.rect(self.screen, self.color, (self.position, self.size))

    def on_mouse_hover(self):
        if self.is_mouse_over():
            return True

    def on_mouse_click(self):
        if self.is_mouse_over() and self.is_mouse_clicked(1):
            return True

    def is_mouse_over(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.position[0] < mouse_pos[0] < self.position[0] + self.size[0] and self.position[1] < mouse_pos[1] < \
                self.position[1] + self.size[1]:
            return True

    @staticmethod
    def is_mouse_clicked(button):
        mouse_buttons = pygame.mouse.get_pressed(3)
        if button == 1:
            return mouse_buttons[0]
        elif button == 2:
            return mouse_buttons[1]
        else:
            return mouse_buttons[3]


class Health_Bar:
    def __init__(self, screen, parent: Player, offset_x=50, offset_y=50, width=200, height=25, background_color=(100, 100, 100), health_color=(100, 200, 100)):
        self.screen = screen
        self.parent = parent
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.background_position = (self.parent.get_player_position()[0] - self.offset_x, self.parent.get_player_position()[1] - self.offset_y)
        self.health_position = (self.background_position[0] - (self.offset_x-5), self.background_position[1] - (self.offset_y-5))
        self.damage_position = self.health_position
        self.background_size = (width, height)
        self.health_size = ((width-10)*(self.parent.player_health/self.parent.max_hp), height-10)
        self.damage_size = (width-10, height-10)
        self.background_color = background_color
        self.health_color = health_color
        self.damage_color = (200, 150, 150)

    def draw_health_bar(self):
        if not self.is_parent_alive():
            return
        pygame.draw.rect(self.screen, self.background_color, (self.background_position, self.background_size))
        pygame.draw.rect(self.screen, self.damage_color, (self.damage_position, self.damage_size))
        pygame.draw.rect(self.screen, self.health_color, (self.health_position, self.health_size))

    def update_position(self):
        if not self.is_parent_alive():
            return
        self.background_position = (self.parent.get_player_position()[0] - self.offset_x, self.parent.get_player_position()[1] - self.offset_y)
        self.health_position = (self.background_position[0] + 5, self.background_position[1] + 5)
        self.damage_position = self.health_position

    def update_health_size(self, damage=10):
        if not self.is_parent_alive():
            return
        self.parent.player_health -= damage
        self.health_size = (self.damage_size[0]*(self.parent.player_health/self.parent.max_hp), self.health_size[1])

    def is_parent_alive(self):
        if self.parent.player_health > 0:
            return True
        return False


class Status_Bar(pygame.sprite.Sprite):
    def __init__(self, color=(100, 100, 100), pos_x=0, pos_y=0, width=200, height=25):
        super().__init__()
        self.width = width
        self.height = height
        self.off_width = width
        self.off_height = height
        self.max_width = width
        self.hp_color = (100, 200, 100)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.bar_group = pygame.sprite.Group(self)
        self.foreground = None

    def add_foreground(self, offset_x=10, offset_y=10, empty_color=(100, 100, 100)):
        self.off_width = self.width - offset_x
        self.max_width = self.off_width
        self.off_height = self.height - offset_y
        self.foreground = pygame.sprite.Sprite()
        self.foreground.image = pygame.Surface([self.off_width, self.off_height])
        self.foreground.image.fill(self.hp_color)
        self.foreground.rect = self.foreground.image.get_rect()
        self.foreground.rect.center = self.rect.center
        empty = pygame.sprite.Sprite()
        empty.image = pygame.Surface([self.width-offset_x, self.height-offset_y])
        empty.image.fill(empty_color)
        empty.rect = empty.image.get_rect()
        empty.rect.center = self.rect.center
        self.bar_group.add(empty)
        self.bar_group.add(self.foreground)

    def draw(self, screen):
        self.bar_group.draw(screen)

    def update_pos(self, parent=None, offset_x=-50, offset_y=35):
        if parent:
            self.off_width = (self.max_width*(parent.player_health/parent.max_hp))
            self.foreground.image = pygame.Surface([self.off_width, self.off_height])
            self.foreground.image.fill(self.hp_color)

        for sprite in self.bar_group:
            if parent:
                sprite.rect.center = [parent.player_position[0]-offset_x, parent.player_position[1]-offset_y]
            else:
                sprite.rect.center = [self.pos_x, self.pos_y]
