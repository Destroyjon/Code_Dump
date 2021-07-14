import pygame
import player_class

screen = pygame.display.set_mode((500, 500))
screen.fill((200, 175, 200))

player = player_class.Player(screen, (200, 200), (100, 100), (90, 150, 90))


def draw_screen():
    screen.fill((150, 175, 200))
    player.draw_player()


def main():
    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_screen()
        pygame.display.update()
        player.update_player_position(10)
    return


if __name__ == "__main__":
    main()
