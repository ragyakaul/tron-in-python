import pygame
import settings
import random
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT


pygame.init()


width = settings.SCREEN_WIDTH
height = settings.SCREEN_HEIGHT

displaySurface = pygame.display.set_mode((width, height))



pygame.display.set_caption("Tron in Python")

player_x: int = width/2
player_y: int = height/2


clock = pygame.time.Clock()
vel = 10

direction = None

# Needs to step 10 at a time

coord_list = [] # example: [[0, 10, false], [0, 20, false]]
for x in range(0, width, 10):
    coord_deets = []
    for y in range(0, height, 10):
        coord_deets.append(y)
        # coord_deets = []
        # coord_deets.append(x)
        # coord_deets.append(y)
        # coord_deets.append(False)
        # coord_list.append(coord_deets)
        # coord_list.append(0)
    coord_list.append(random.randint(0, 1000000000))

 # Come back and ask Clinton       

print("PRINT STATEMENTS")
print(coord_list)
print("PRINT STATEMENTS END")


# def markandCheckCoordinate():
#     print(coord_list[int(player_x)][2])
    
#     if coord_list[int(player_x)][2] == True:
#         print("TAIL HIT!!!")
#         exit()
    
#     if player_x == coord_list[int(player_x)][0]:
#         if player_y == coord_list[int(player_x)][1]:
#             coord_list[int(player_x)][2] = True


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

    if direction == "UP":
        player_y -= vel
        print(f"player_y UP: {player_y}")
        #markandCheckCoordinate()
        
    if direction == "DOWN":
        player_y += vel
        print(f"player_y DOWN: {player_y}")
        #markandCheckCoordinate()

    if direction == "LEFT":
        player_x -= vel
        print(f"player_x LEFT: {player_x}")
        #markandCheckCoordinate()
        
    if direction == "RIGHT":
        player_x += vel
        print(f"player_x RIGHT: {player_x}")
        #markandCheckCoordinate()


    #logic for if it goes out of the screen end game? (original game freezes with a bang sound)
    if player_y > height or player_y < 0 or player_x > width or player_y < 0:
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


            




