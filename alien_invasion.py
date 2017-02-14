#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s %(levelname)-5s - %(message)s'
)

import pygame
from pygame.sprite import Group

import game_functions as gf
from settings   import Settings
from ship       import Ship
from game_stats import GameStats
from button     import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(ai_settings)
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()
    play_button = Button(ai_settings, screen, 'Play')
    scoreboard = Scoreboard(ai_settings, screen, stats)

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets, scoreboard, stats)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        logging.debug("total bullets: %d", len(bullets))
        gf.update_screen(ai_settings, screen, stats, scoreboard, ship, aliens, bullets, play_button)

run_game()
