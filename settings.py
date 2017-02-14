#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class Settings():
    """Save all settings"""

    def __init__(self):
        self.screen_width  = 1200
        self.screen_height = 800
        self.bg_color      = (230, 230, 230)

        self.ship_limit = 3

        self.bullet_width    = 3
        self.bullet_height   = 10
        self.bullet_color    = 60, 60, 60
        self.bullets_allowed = 10

        self.fleet_drop_speed = 20

        self.speedup_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor   = 8
        self.bullet_speed_factor = 30
        self.alien_speed_factor  = 2

        self.alien_points = 50

        self.fleet_direction = 1  # 1 for right; -1 for left

    def increase_speed(self):
        self.ship_speed_factor   *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor  *= self.speedup_scale

        self.alien_points *= 2
