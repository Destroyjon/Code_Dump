import pygame


def debug(state=False):
    return state


class Player:
    def __init__(self, screen, location=[0, 0], size=(10, 10), color=(0, 0, 0)):
        self.screen = screen
        self.player_position = location
        self.player_size = size
        self.player_color = color
        self.death_color = (50, 50, 50)
        self.max_hp = 200
        self.player_health = 100
        print(f"Player Health = {self.max_hp}/{self.player_health}")

    def set_player_position(self, location):
        self.player_position = location

    def get_player_position(self):
        return self.player_position

    def draw_player(self):
        if self.player_health <= 0:
            color = self.death_color
        else:
            color = self.player_color
        return pygame.draw.rect(self.screen, color, (self.player_position, self.player_size))

    @staticmethod
    def get_input_direction():
        keys = pygame.key.get_pressed()
        up = keys[pygame.K_w]
        down = keys[pygame.K_s]
        left = keys[pygame.K_a]
        right = keys[pygame.K_d]
        key_values = [up, down, left, right]
        speed = 2
        if keys[pygame.K_LSHIFT]:
            speed = 5
        # Directional Values for movement
        d_up = (0, -1*speed)
        d_down = (0, 1*speed)
        d_left = (-1*speed, 0)
        d_right = (1*speed, 0)

        active_keys = 0
        for state in key_values:
            active_keys += state

        # Check for amount of movement keys being pressed
        if active_keys == 0 or active_keys == 4:
            idle = (0, 0)
            return idle
        elif active_keys == 1:
            # Check which key is being pressed and return direction
            if up:
                return d_up
            elif down:
                return d_down
            elif left:
                return d_left
            else:
                return d_right
        else:
            total_movement = (0, 0)
            if up:
                total_movement = Player.add_tuples(total_movement, Player.mult_tuple(d_up, 0.75))
            if down:
                total_movement = Player.add_tuples(total_movement, Player.mult_tuple(d_down, 0.75))
            if left:
                total_movement = Player.add_tuples(total_movement, Player.mult_tuple(d_left, 0.75))
            if right:
                total_movement = Player.add_tuples(total_movement, Player.mult_tuple(d_right, 0.75))
            return total_movement

    def update_player_position(self, step=1):
        if self.player_health > self.max_hp:
            self.player_health = self.max_hp
        if self.player_health > 0:
            self.player_position = self.add_tuples(self.player_position, self.get_input_direction())


    @staticmethod
    def add_tuples(tuple_a, tuple_b) -> tuple:
        total_tuple = [0, 0]
        for i in range(len(tuple_a)):
            total_tuple[i] = total_tuple[i] + tuple_a[i]
            total_tuple[i] = total_tuple[i] + tuple_b[i]
        return total_tuple

    @staticmethod
    def mult_tuple(tuple_a, number: float) -> tuple:
        total_tuple = [0, 0]
        for i in range(len(tuple_a)):
            total_tuple[i] = tuple_a[i] * number
        return total_tuple
