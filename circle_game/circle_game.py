import pygame, sys
from circle import Circle
from player import Player
import game_functions as game_functions
from settings import Settings


def main():
    """This main method will run circle_game using helper methods and classes"""
    pygame.init()

    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_size)
    pygame.display.set_caption('Colin\'s Circle Conundrum')
    player = Player(screen)

    game_running = True

    # Two separate while loops exist, one dictating the overall game and one for each round
    while game_running:
        settings.round_num += 1

        round_running = True

        circle_list = []

        # Circles being spawed will be the round number times 2 for progressive difficulty
        for x in range(settings.round_num*2):
            circle = Circle(screen, x)
            circle_list.append(circle)

        # Main loop runs until collision
        while round_running:
            screen.fill(settings.background_color)

            game_functions.check_events(player)

            # Update all circles
            for circle in circle_list:
                circle.update()

            # Updates player location based on game_function user input listening
            player.update()

            # Returns True if collision occurs
            game_functions.detect_collision(circle_list, player)

            # End game if out of lives
            if player.lives <= 0:
                round_running = False
                game_running = False

            # End round complete, player makes it to top then reset round
            if game_functions.check_round_complete(player):
                round_running = False

            game_functions.update_text(screen, settings, player)

            # Puts out new screen, oygames "animation" effect
            pygame.display.flip()

            # Balls were moving to slow so this is how I sped them up
            pygame.time.delay(2)

    # Once the game is over, all lives expired user is presented with option to play another round
    end_game = True

    while end_game:
        game_functions.end_game(screen, settings, player)
        game_functions.update_text(screen, settings, player)
        pygame.display.flip()

        # Check if user wants to play again if not we terminate, otherwise we start over
        if game_functions.check_end_events():
            main()

        # Can slow this process down so as to not eat up too much resources
        pygame.time.delay(100)


# Starts game
main()





