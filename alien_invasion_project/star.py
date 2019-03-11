import pygame
from random import randint

class Star():
    """A class to represent stars on background."""

    def __init__(self, ai_settings, screen):
        """Initialize star."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the star image and set its rect attribute.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each alien near the top left of the screen.

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the alien at its currentlocation."""
        random_number = randint(-5,10)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.screen.blit(self.image, self.rect)
