import pygame
class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (76, 82, 82)

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 4
        self.bullet_height = 25
        self.bullet_color = 244, 220, 66
        self.bullets_allowed = 3

        # The current mode of ship's gun
        self.gun_current_mode = 'simple'

        # Alien settings
        self.alien_speed_factor = 4
        self.fleet_drop_speed = 3
        # fleet_direction of 1 represent right; -1 represent left.
        self.fleet_direction = 1
