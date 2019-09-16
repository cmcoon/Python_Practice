import sys, pygame

class Player():
    """Player objects contain methods and settings regarding small block appearance and movement"""

    def __init__(self, screen):
        """Initializes player object as small white block, start position is bottom center"""
        self.player_color = (237, 221, 190)
        self.player_speed = 1

        # Y axis is reversed in positive direction in pygame
        self.startx = 396
        self.starty = 575

        self.xpos = self.startx
        self.ypos = self.starty

        self.width = 9
        self.length = 15

        # Creates actual rectangle object
        self.rect = pygame.Rect(self.xpos, self.ypos, self.width, self.length)

        self.screen = screen

        # Up and down variables will change to true if ey up or down is pressed in game functions
        self.up = False
        self.down = False
        self.lives = 3

    def update(self):
        """Method updates player position based on if up/down key is pressed and if within screen limits"""
        if self.up and self.ypos >= 5:
            self.ypos -= self.player_speed
        elif self.down and self.ypos <= 590:
            self.ypos += self.player_speed

        self.rect.y = self.ypos

        # Draw the rectangle in the new location, when flipped in main method this will show
        pygame.draw.rect(self.screen, self.player_color, self.rect)

    def reset_pos(self):
        """Method used when player completes round and resets player to start position"""
        self.ypos = self.starty
        self.xpos = self.startx





