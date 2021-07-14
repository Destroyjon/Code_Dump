# TODO: Make a world map for Squares


def tile_generator(num_tiles, tile_width, tile_height):
    tile = {}
    i = 0
    for n in range(num_tiles):
        temp = []
        for y in range(tile_height):
            for x in range(tile_width):
                temp += [(x + i, y + i)]
        tile.update({n + 1: temp})
        i += int(tile_width * tile_height / 2)
    return tile


def world(width, height, tile_width, tile_height):
    total_tiles = int((width * height) / (tile_width + tile_height))
    print(total_tiles)
    world = [tile_generator(total_tiles, tile_width, tile_height)]
    print(world)


class Cell:
    def __init__(self, location, living_status=False):
        self.location = location
        self.living_status = living_status
        self.neighbours = None

    def is_alive(self):
        if not self.living_status:
            return
        return self.living_status

    def set_living_status(self, living_status):
        self.living_status = living_status

    def get_living_status(self):
        return self.living_status

    def get_location(self):
        return self.location

    def set_neighbours(self):
        center = self.get_location()
        x = center[0]
        y = center[1]
        up = [x, y - 1]
        right_up = [x + 1, y - 1]
        right = [x + 1, y]
        right_down = [x + 1, y + 1]
        down = [x, y + 1]
        left_down = [x - 1, y + 1]
        left = [x - 1, y]
        left_up = [x - 1, y - 1]
        self.neighbours = [up, right_up, right, right_down, down, left_down, left, left_up]


world(10, 10, 2, 2)


[1, 0, 0]
[0, 1, 1]
[1, 1, 0]

[0, 0, 0, 0, 0]
[0, 1, 0, 0, 0]
[0, 0, 1, 1, 0]
[0, 1, 1, 0, 0]
[0, 0, 0, 0, 0]

for cell in cells:
    insert.top(0)
    insert.bottom(0)
for len(cell+2):
    [].append(0)
insert.top/bottom

if