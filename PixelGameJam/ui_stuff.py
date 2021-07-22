import pygame
from player_class import Player


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.x = x
        self.y = y
        self.x_point = x-width/2
        self.y_point = y-height/2
        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.Surface([width, height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.button_function = None
        self.pressed = 0

    def __repr__(self):
        return f"{self.rect.center}, {self.rect.size}, {self.color}"

    def __set_name__(self, name):
        self.__name__ = name

    def reset(self, reset_size=False):
        if reset_size:
            self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]

    def on_hover(self):
        if self.is_mouse_over():
            self.image = pygame.Surface([self.width + 5, self.height + 5])

    def on_click(self):
        if self.is_pressed():
            self.image = pygame.Surface([self.width + 10, self.height + 10])
            if self.pressed == 0:
                self.pressed = 1
                return self.get_button_action()
        else:
            self.pressed = 0

    def is_mouse_over(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.x_point < mouse_pos[0] < self.x_point + self.width and self.y_point < mouse_pos[1] < \
                self.y_point + self.height:
            return True

    def is_pressed(self):
        if self.is_mouse_over():
            if pygame.mouse.get_pressed(3)[0]:
                return True

    def is_button_usable(self):
        if pygame.mouse.get_pressed(3)[0]:
            self.pressed = 1
        else:
            self.pressed = 0
        return self.is_pressed()


    def set_button_action(self, function):
        self.button_function = function

    def get_button_action(self):
        if self.button_function:
            self.button_function()
        else:
            return None

    def update(self):
        if self.is_mouse_over():
            self.on_hover()
            self.on_click()
            self.reset(False)
        else:
            self.reset(True)


class Skill_Button(Button):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)


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
        for sprite in self.bar_group:
            if parent:
                sprite.rect.center = [parent.player_position[0]-offset_x, parent.player_position[1]-offset_y]
            else:
                sprite.rect.center = [self.pos_x, self.pos_y]

    def update_parent_data(self, parent):
        self.off_width = (self.max_width*(parent.player_health/parent.max_hp))
        self.foreground.image = pygame.Surface([self.off_width, self.off_height])
        self.foreground.image.fill(self.hp_color)

    def set_pos(self, x, y):
        self.pos_x = x
        self.pos_y = y
