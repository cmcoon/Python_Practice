import pygame, sys, random

class Circle():
    """Circle class used to create circle objects which player is not allowed to collide with"""

    def __init__(self, screen, id):
        """Method is meant to initialize one circle object with awareness that many circles will be spawned"""

        # Creates buffer zone at top and bottom, also spawning circles in multiples of 20 since radius is 10
        # More than one circle can spawn in same horizontal path, is random
        # Note circle_coordinates[0] is x axis and circle_coordinates[1] is y coordinate
        self.circle_coordinates = [(random.randint(10,790)), (random.randint(5, 25)*20)]
        self.circle_color = (169, 169, 169)
        self.circle_speed = 1
        self.moving_right = False
        self.moving_left = False
        self.circle_radius = 10

        self.id = id

        self.screen = screen

        # Direction circle is moving will be left or right
        random_direction_selector = random.randint(1, 2)

        # Direction circle is moving based off which side of screen circle hit last
        if random_direction_selector == 1:
            self.right_hit = True
            self.left_hit = False
        else:
            self.right_hit = False
            self.left_hit = True

    def update(self):
        """Method detects for circle hitting screen edge, if so direction is reversed"""
        if self.circle_coordinates[0] == 790:
            self.right_hit = True
            self.left_hit = False
        if self.circle_coordinates[0] == 10:
            self.right_hit = False
            self.left_hit = True

        # Here direction of circle is dictated by plus or minus x coordinate
        if self.right_hit == True and self.left_hit == False:
            self.circle_coordinates[0] -= 1
        elif self.right_hit == False and self.left_hit == True:
            self.circle_coordinates[0] += 1

        # Updates the individual circle based on direction and position
        pygame.draw.circle(self.screen, self.circle_color, self.circle_coordinates, self.circle_radius)

