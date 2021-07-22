import pygame
import player_class
import ui_stuff
import scene

WIDTH = 1000
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((200, 175, 200))

player = player_class.Player(screen, (WIDTH / 2 - 50, HEIGHT / 2 - 50), (100, 100), (90, 150, 90))
# reset_button = ui_stuff.Button(100, 75, 100, 50, (100, 100, 100))
skill_button = ui_stuff.Skill_Button(100, 75, 100, 50, (100, 100, 100))


def damage_button():
    if player.player_health > 0:
        player.player_health -= 50
        print(f"Player Health = {player.max_hp}/{player.player_health}")
    else:
        print(f"Player Health = {player.max_hp}/{player.player_health}")
        print("PLAYER HAS DIED")
        player.player_health += 200


skill_button.set_button_action(damage_button)

hp_bar = ui_stuff.Status_Bar(pos_x=200, pos_y=(HEIGHT-HEIGHT/3)-25, width=400, height=50)
hp_bar.add_foreground(empty_color=(200, 150, 150))

battle_scene = scene.BattleScene(WIDTH, HEIGHT)
# battle_scene.add_buttons(reset_button)
battle_scene.add_buttons(skill_button)


def draw_screen():
    screen.fill((150, 175, 200))
    battle_scene.draw(screen)
    player.draw_player()
    hp_bar.draw(screen)


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
        hp_bar.update_parent_data(player)
        battle_scene.update()
    return


if __name__ == "__main__":
    main()
