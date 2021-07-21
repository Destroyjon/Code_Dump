import pygame
import ui_stuff


class MainMenu:
    def __init__(self):
        self.menu = 0

    def get_menu(self):
        return self.menu


class BattleScene:
    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        self.screen.fill((200, 200, 233))
