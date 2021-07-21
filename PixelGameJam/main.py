import pygame
import player_class
import ui_stuff

WIDTH = 1000
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((200, 175, 200))

player = player_class.Player(screen, (WIDTH/2-50, HEIGHT/2-50), (100, 100), (90, 150, 90))
reset_button = ui_stuff.Button(screen, (25, HEIGHT - 75), (100, 50), (100, 100, 100))
base_size_button = reset_button.get_button_size()

hp_bar = ui_stuff.Status_Bar()
hp_bar.add_foreground(empty_color=(200, 150, 150))


def draw_screen():
    screen.fill((150, 175, 200))
    player.draw_player()
    reset_button.draw_button()
    hp_bar.draw(screen)


def main():
    running = True
    mouse_click = 0
    clock = pygame.time.Clock()
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_screen()

        pygame.display.update()
        player.update_player_position(10)
        hp_bar.update_pos(player)
        if reset_button.on_mouse_hover():
            reset_button.set_button_size((105, 55))
        else:
            reset_button.set_button_size(base_size_button)

        if reset_button.on_mouse_click():
            if mouse_click == 0:
                mouse_click = 1
                if player.player_health > 0:
                    player.player_health -= 50
                    print(f"Player Health = {player.max_hp}/{player.player_health}")
                else:
                    print(f"Player Health = {player.max_hp}/{player.player_health}")
                    print("PLAYER HAS DIED")
                    player.player_health += 200
        else:
            mouse_click = 0
    return


if __name__ == "__main__":
    main()
