import pygame

class Settings():
    """This class is used to store various gamee settings for circle_game"""

    def __init__(self):
        """Initializes settings required for game operation"""
        self.round_num = 0
        self.screen_size = (800, 600)
        self.background_color = (11, 7, 138)

        self.font = pygame.font.SysFont("comicsansms", 16)

        # These are mainly to be used for game objects
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.silver = (128, 128, 128)


