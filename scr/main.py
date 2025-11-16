import pygame as pg
from map import Map

import sys

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
WINDOW_CENTER_X = WINDOW_WIDTH // 2
WINDOW_CENTER_Y = WINDOW_HEIGHT // 2
TILE_SIZE = 64

# Initialize Pygame
pg.init()
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Game Window")
clock = pg.time.Clock()

def main():
    game_map = Map()
    game_map.set_tile_size(TILE_SIZE)

    player = pg.image.load('scr/assets/image/1.png').convert_alpha()
    player = pg.transform.scale(player, (TILE_SIZE, TILE_SIZE))

    # Game loop
    running = True
    while running:

        # Event handling
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_s:
                    game_map.move_down()
                elif event.key == pg.K_w:
                    game_map.move_up()
                elif event.key == pg.K_a:
                    game_map.move_left()
                elif event.key == pg.K_d:
                    game_map.move_right()
                

        screen.fill((240, 210, 60))
        # Render game elements here
        screen.blit(game_map.rendered_surface, game_map.on_screen(WINDOW_CENTER_X, WINDOW_CENTER_Y))
        screen.blit(player, (WINDOW_CENTER_X - TILE_SIZE // 2, WINDOW_CENTER_Y - TILE_SIZE // 2))


        pg.display.flip()
        clock.tick(60)
    pg.quit()

if __name__ == "__main__":
    main()
