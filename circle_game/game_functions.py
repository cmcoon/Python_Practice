import sys, pygame, math


def check_events(player):
    """Main event checking method to detect quit, or if key is pressed"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            key_down_events(event, player)
        if event.type == pygame.KEYUP:
            key_up_events(event, player)


def key_down_events(event, player):
    """Method handles if a key is pressed down events"""
    if event.key == pygame.K_UP:
        player.up = True
        player.down = False
    if event.key == pygame.K_DOWN:
        player.up = False
        player.down = True


def key_up_events(event, player):
    """Method handles events when a key is released"""
    if event.key == pygame.K_UP:
        player.up = False
        player.down = False
    if event.key == pygame.K_DOWN:
        player.up = False
        player.down = False


def check_end_events():
    """Method is specifically for endgame events, mainly K_RETURN restarts game"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return True
    return False


def check_round_complete(player):
    """Method does not require key event, just check if block has surpassed obstacles"""
    if player.ypos <= 30:
        player.reset_pos()
        return True
    return False


def lives_left(player):
    """Returns true if player has lives left"""
    if player.lives > 0:
        return True
    return False


def update_text(screen, settings, player):
    """Method handles round and lives left text elements"""
    round_text = settings.font.render("Round: " + str(settings.round_num), False, settings.white)
    screen.blit(round_text, (10, 8))

    lives_text = settings.font.render("Lives Left: " + str(player.lives), False, settings.white)
    screen.blit(lives_text, (698, 8))


def end_game(screen, settings, player):
    """Method displays endgame message"""
    end_text = settings.font.render("Game Over Press Enter to Play Again", False, settings.white)
    screen.blit(end_text, (265, 285))


def detect_collision(circle_list, player):
    """Crude collision detection method"""
    pwidth_half = player.width / 2
    plength_half = player.length / 2

    radius = circle_list[0].circle_radius

    player_diag_mag = math.sqrt(abs(pwidth_half ** 2 + plength_half ** 2))
    max_diag_dist = player_diag_mag + radius

    for circle in circle_list:
        circlex = circle.circle_coordinates[0]
        circley = circle.circle_coordinates[1]

        playerx = player.xpos
        playery = player.ypos

        # Detect collision based of difference in center points being less than max allowable
        mag_btwn_centers = math.sqrt(((circlex - playerx)**2) + ((circley - playery)**2))

        if mag_btwn_centers <= max_diag_dist:
            #print('collision ' + str(circle.id))
            player.reset_pos()
            player.lives -= 1
            #print(player.lives)


