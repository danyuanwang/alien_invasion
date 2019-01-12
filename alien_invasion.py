import pygame

from ship import Ship
from alien import Alien

import game_functions as gf
from settings import Settings
from pygame.sprite import Group



def run_game():
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    alien = Alien(ai_settings, screen)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens= Group()
    gf.create_fleet(ai_settings, screen, ship, aliens, bullets)
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        ship.blitme()
        bullets.update()
        #get rid of bullets that have disappeared
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
run_game()
