import pygame


pygame.init()

pygame.display.set_caption("PONG")

# COLORS
red: int = (250, 0, 0)
white = (255, 255, 255)
blue: int = (0, 0, 250)
black: int = (0, 0, 0)

# SCREEN
screen_width: int = 800
screen_height: int = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# OBJECTS
player_1 = pygame.Rect((10, 250, 10, 70))
player_2 = pygame.Rect((780, 250, 10, 70))
floor = pygame.Rect(0, 600, 800, 50)
roof = pygame.Rect(0, -50, 800, 50)

# SCORE
point_1 = 0
point_2 = 0

# BALL
start_cords = (screen_width // 2, screen_height // 2)
puck = pygame.Rect((start_cords[0], start_cords[1], 10, 10))
speed = [5,5] 


# GAME CLOCK
clock = pygame.time.Clock()

run = True
while run:
    # FRAME RATE
    clock.tick(60)

    # CREATING SPRITES
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (white), player_1)
    pygame.draw.rect(screen, (white), player_2)
    pygame.draw.rect(screen, (white), floor)
    pygame.draw.rect(screen, (white), roof)
    pygame.draw.ellipse(screen, (white), puck)

    # PLAYERS LOGIC
    key = pygame.key.get_pressed()
    old_position = player_1.copy()

    if key[pygame.K_s]:
        player_1.move_ip(0, 5)
    if key[pygame.K_w]:
        player_1.move_ip(0, -5)

    if player_1.colliderect(floor) or player_1.colliderect(roof):
        player_1 = old_position

    key = pygame.key.get_pressed()
    old_position = player_2.copy()

    if key[pygame.K_DOWN]:
        player_2.move_ip(0, 5)
    if key[pygame.K_UP]:
        player_2.move_ip(0, -5)

    if player_2.colliderect(floor) or player_2.colliderect(roof):
        player_2 = old_position

    
    # BALL LOGIC
    puck.move_ip(speed)

    if puck.colliderect(floor):
        speed[1] = -abs(speed[1])
    if puck.colliderect(roof):
        speed[1] = abs(speed[1])
    if puck.colliderect(player_1):
        speed[0] = abs(speed[0])
    if puck.colliderect(player_2):
        speed[0] = -abs(speed[0])
    
    # SCORING LOGIC 
    if puck.x < 0:
        puck.topleft = start_cords
        point_2 = point_2 + 1
        print("P2: " + str(point_2))

    if puck.x > 800:
        puck.topleft = start_cords
        point_1 = point_1 + 1
        print("P1: " + str(point_1))


    # END GAME LOGIC
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
