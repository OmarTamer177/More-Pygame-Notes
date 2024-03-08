###################################################################
#Collisions in pygame
#
# We always use rects for collisions:
# rect1.colliderect(rect2) 
# or
# rect.collidepoint((x,y))
#
# An approach to check for collisions:
# 1.use colliderect() method
# 2.calculate the position of the collision for each side
# for example: if bottom of rect1 - top of rect2 == 0
# that means there is a collision with the bottom side of rect1
###################################################################

import pygame, sys

pygame.init()

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

#Creating 2 rectangles and specifying their speeds
moving_rect = pygame.Rect(350, 350, 60, 60)
velocity_x = 5
velocity_y = 4

static_rect = pygame.Rect(300, 600, 300, 50)
static_rect.center = (300, 500)
static_velocity = 2

collision_tolerence = 10

while True:
    screen.fill((30,30,30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Bouncing rects logic
    moving_rect.x += velocity_x
    moving_rect.y += velocity_y

    static_rect.y += static_velocity

    #check for collisions of the static rect with the border of the screen
    if static_rect.bottom > 600 or static_rect.top < 0:
        static_velocity = -static_velocity

    #check for collisions of the moving rect with the border of the screen
    # We use velocity = abs(velocity) to force the object to move to the +ve direction
    # and velocity = -abs(velocity) to force the object to move to the -ve direction
    #NOTE: Using velocity = -velocity could lead to breakage on certain positions
    if moving_rect.right > 600:              #if it passes the right boundary  
        velocity_x = -abs(velocity_x)        #move left
    if moving_rect.left < 0:                 #if it passes the left boundary  
        velocity_x = abs(velocity_x)         #move right
    if moving_rect.bottom > 600:             #if it passes the bottom boundary  
        velocity_y = -abs(velocity_y)        #move up
    if moving_rect.top < 0:                  #if it passes the top boundary  
        velocity_y = abs(velocity_y)         #move down

    #Collisions between rects
    #using the same techinque with the walls
    if moving_rect.colliderect(static_rect):
        if abs(moving_rect.bottom - static_rect.top) < collision_tolerence:
            velocity_y = -abs(velocity_y)
        if abs(moving_rect.top - static_rect.bottom) < collision_tolerence:
            velocity_y = abs(velocity_y)
        if abs(moving_rect.left - static_rect.right) < collision_tolerence:
            velocity_x = abs(velocity_x)
        if abs(moving_rect.right - static_rect.left) < collision_tolerence:
            velocity_x = -abs(velocity_x)

    pygame.draw.rect(screen, 'white', static_rect)
    pygame.draw.rect(screen, 'red', moving_rect)

    pygame.display.update()
    clock.tick(60)