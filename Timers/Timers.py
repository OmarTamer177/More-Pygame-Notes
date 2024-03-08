############################################################################
# Timers
# The logic of timers 
#            .-------------------.--------------------.
# start time ^      static point ^       current time ^
#
# Implementation:
# The timer is the difference between the static poinr and current time
############################################################################
import pygame, sys

#Timer starts when initializing pygame
#current time = 0
pygame.init()

screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()

current_time = 0
static_point = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #Check for the desired event for the timer to start and set an anchor point
        if event.type == pygame.MOUSEBUTTONDOWN:
            static_point = pygame.time.get_ticks()
            screen.fill('white') #Dummy code(can be replaced)

    #Check for when the timer finishes, another event will happen
    current_time = pygame.time.get_ticks()
    if current_time - static_point >= 2000:
        screen.fill('black') #Dummy code(can be replaced)

    pygame.display.update()
    clock.tick(60)