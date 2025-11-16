from json import load
from pygame import Surface, image, transform
class Map:
    def __init__(self, name = "map1", tile_size=64):
        self.tile_size = tile_size
        path = f'scr/assets/map/{name}.json'
        with open(path, 'r') as f:
            self.data = load(f)
            self.width = self.data['width']
            self.height = self.data['height']
            self.tiles = self.data['tiles']

        self.rendered_surface = self.render()

        self.player_pos = self.data.get('playerStart', [0, 0])
   
    def on_screen(self, player_on_screen_x, player_on_screen_y):
        return (player_on_screen_x - (self.player_pos[0] + 0.5) * self.tile_size, player_on_screen_y - (self.player_pos[1] + 0.5) * self.tile_size)
    
    def set_tile_size(self, size):
        self.tile_size = size
        self.rendered_surface = self.render()

    def get_tile(self, x, y):
        return self.tiles[y][x]

    def render(self):
        surface = Surface((self.width * self.tile_size, self.height * self.tile_size))
        surface.fill((40, 250, 40))
        pixel_wall = image.load('scr/assets/image/wall1.png')  
        pĩell_wall = transform.scale(pixel_wall, (self.tile_size, self.tile_size))

        for y in range(self.height):
            for x in range(self.width):
                tile = self.get_tile(x, y)
                if tile == 1:
                    surface.blit(pĩell_wall, (x * self.tile_size, y * self.tile_size))

        return surface

    def move_up(self):
        if self.player_pos[1] > 0 and self.get_tile(self.player_pos[0], self.player_pos[1] - 1) == 0:
            self.player_pos[1] -= 1
            return True
        return False
    def move_down(self):
        if self.player_pos[1] < self.height - 1 and self.get_tile(self.player_pos[0], self.player_pos[1] + 1) == 0:
            self.player_pos[1] += 1
            return True
        return False
    def move_left(self):
        if self.player_pos[0] > 0 and self.get_tile(self.player_pos[0] - 1, self.player_pos[1]) == 0:
            self.player_pos[0] -= 1
            return True
        return False
    def move_right(self):
        if self.player_pos[0] < self.width - 1 and self.get_tile(self.player_pos[0] + 1, self.player_pos[1]) == 0:
            self.player_pos[0] += 1
            return True
        return False
    