import pygame
import settings
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT


pygame.init()

#displaySurface = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

displaySurface = pygame.display.set_mode((30, 30))



pygame.display.set_caption("Tron in Python")

#player_x: int = settings.SCREEN_WIDTH/2
#player_y: int = settings.SCREEN_HEIGHT/2

player_x: int = 15
player_y: int = 15

clock = pygame.time.Clock()
vel = 10

direction = None

# Needs to step 10 at a time
coord_list = [] # example: [[0, 10, false], [0, 20, false]]
for x in range(0, 30, 10):
    for y in range(0, 30, 10):
        coord_deets = []
        coord_deets.append(x, y)
        #coord_deets.append(y)
        coord_deets.append(False)
        coord_list.append(coord_deets)

print(coord_list)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = "UP"
            elif event.key == pygame.K_DOWN:
               direction = "DOWN"
            elif event.key == pygame.K_LEFT:
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT:
                direction = "RIGHT"

    """
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_UP]:
        player_y = player_y - vel
    if pressed_keys[K_DOWN]:
        player_y = player_y + vel
    if pressed_keys[K_LEFT]:
        player_x = player_x - vel
    if pressed_keys[K_RIGHT]:
        player_x = player_x + vel
    """

    print[f"coord_list[player_x, player_y] {coord_list[player_x, player_y]}"]
    if direction == "UP":
        player_y -= vel
        print(f"player_y UP: {player_y}")
    if direction == "DOWN":
        player_y += vel
        print(f"player_y DOWN: {player_y}")
    if direction == "LEFT":
        player_x -= vel
        print(f"player_x LEFT: {player_x}")
    if direction == "RIGHT":
        player_x += vel
        print(f"player_x RIGHT: {player_x}")


    #logic for if it goes out of the screen end game? (original game freezes with a bang sound)
    if player_y > 100 or player_y < 0 or player_x > 100 or player_y < 0:
        pygame.quit()
        exit()

    player = pygame.surface.Surface((10, 10))
    player.fill((255, 255, 255))
    displaySurface.blit(player, (player_x, player_y)) # Is there something like you set this special flag to 1 and now write logic that if you approach anything with a 1 the game ends?
    # Maybe just appending to a dictionary? Append the coordinates & then if the coordinates are present you end the game? 
    # Can we use a hash table? Add the coordinates to a hash table. Now if any combo of player_x & player_y is present in the hash table, you end the game. DO a retrieval and check. 
    
    pygame.display.update()


    fps = clock.get_fps()
    print(f"FPS: {fps}")
    print(f"x: {player_x}, y: {player_y}")
    clock.tick(10)

    # Mark the coordinate the player has been on as 'checked', if the player approaches the same coordinate, quit game. 


            




