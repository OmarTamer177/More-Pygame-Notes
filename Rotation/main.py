##########################################################################
# Rotation
#
# done using: pygame.transform.rotozoom() or pygame.transform.rotate()
# although rotozoom() applies a filter to improve quality
#
# Quality control: The more rotating the worse the quality gets
##########################################################################

import pygame, sys

pygame.init()

screen = pygame.display.set_mode((900, 600)) 
clock = pygame.time.Clock()


#Make the surface to be rotated
#pygame.SRCALPHA argument removes the background of a rotated surface
snail = pygame.Surface((100,100), pygame.SRCALPHA)
#snail = pygame.image.load('Assets/snail.png')
snail_rect = snail.get_rect(center=(450, 300))
snail.fill('red')

#initialize the angle with 0
angle = 0

while True:
    screen.fill('white')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #as time passes the angle increases slightly
    angle += 0.2

    #make a copy of the object to be rotated to be able to rotate from the original object
    #that prevents the loss of quality
    rotated_snail = pygame.transform.rotozoom(snail, angle, 2)
    rotated_snail_rect = rotated_snail.get_rect(center=(450, 300))

    screen.blit(rotated_snail, rotated_snail_rect)
    pygame.display.update()
    clock.tick(240)
