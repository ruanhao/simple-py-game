#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(
    # level = logging.DEBUG,
    format = '%(asctime)s %(levelname)-5s - %(message)s'
)

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        logging.info("total bullets: %d", len(bullets))
        gf.update_screen(ai_settings, screen, ship, alien, bullets)

run_game()
