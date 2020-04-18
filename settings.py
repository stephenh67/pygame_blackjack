import pygame


class Settings:
    """ A class to store blackjack settings """

    def __init__(self):
        """ Initialize the game's static settings. """
        # screen
        self.screen_width = 1200
        self.screen_height = 700
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.bg_color = (22, 84, 8)

        # Define some colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (22, 84, 8)