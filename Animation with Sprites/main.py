#######################################################################
# Animation with Sprites
#
# How animation works:
# Successive images interchanging very fast
#######################################################################

import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = []
        for index in range(1, 11):
            self.sprites.append(pygame.image.load(f'Assets/attack_{index}.png').convert_alpha())
        for index in range(len(self.sprites)):
            self.sprites[index] = pygame.transform.scale_by(self.sprites[index], 4)
        
        self.is_attacking = False
        self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect(center = (250, 250))
    
    #A function that checks for different animations
    def animation(self):
        # For the attaking animation: 
        # itirate throght animation frames, until animation is finished 
        if self.is_attacking:
            self.current_sprite += 1
            # when the animation finish, return the object to its initial state
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_attacking = False
            self.image = self.sprites[self.current_sprite]
        else:
            #can add different animation checking (is_jumping, is_walking, is_healing...)
            pass

pygame.init()

Width = 500
Height = 500
Win_size = (Width, Height)

# ############ screen ###################
screen = pygame.display.set_mode(Win_size)
clock = pygame.time.Clock()
pygame.display.set_caption('Frog animation')

#Frog group
frog = Player()
frog_group = pygame.sprite.GroupSingle()
frog_group.add(frog)
static_point = 0

# ########### Game loop #################
while True:
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # if the certain event happened, the desired action will happen
        if event.type == pygame.MOUSEBUTTONDOWN:
            #save a static point on the timeline and set the animation variable to true
            static_point = pygame.time.get_ticks()
            frog.is_attacking = True
            # Rest of the actions
            # .
            # .

    # If the animation is playing and the timer ticks to a desired time; 
    # change to the next frame
    # until the animation frames ends 
    if frog.is_attacking and pygame.time.get_ticks() - static_point > 50:
        static_point = pygame.time.get_ticks()
        frog.animation()
    
    frog_group.draw(screen)
    pygame.display.update()
    clock.tick(240)
    
