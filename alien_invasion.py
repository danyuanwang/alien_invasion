import sys

import pygame

from ship import Ship

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (90, 180, 200)
    ship = Ship(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()
run_game()
