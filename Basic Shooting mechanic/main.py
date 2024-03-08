####################################################################
# Creating basic Bullet shooting mechanic
#
# bullet logic:
# 1.get position of the player(or whatever shooting the bullet)
# 2.create a bullet in that place
# 3.move the bullet in the desired direction
#
# There are 2 approaches:
# 1.using rectangles and funtions
# 2.using classes and sprites         <--better
####################################################################
import pygame, sys

#player sprite class, follows the mouse and creates bullets
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Assets/spaceship.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 2)
        self.rect = self.image.get_rect(center=(350, 250))

    def update_pos(self):
        self.rect.center = pygame.mouse.get_pos()

    def create_bullet(self):
        return Bullet(pygame.mouse.get_pos())

    def update(self):
        self.update_pos()


#Bullet sprite class, created by player
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('Assets/bullet.png').convert_alpha()
        self.rect = self.image.get_rect(center=(pos[0] + 20, pos[1]))
    
    def update_pos(self):
        self.rect.x += 40

    def check_invalidity(self):
        if self.rect.x > 900:
            self.kill()

    def update(self):
        self.update_pos()

pygame.init()

screen = pygame.display.set_mode((700,500))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

player = Player()
player_group = pygame.sprite.GroupSingle()
player_group.add(player)

bullet_group = pygame.sprite.Group()

while True:
    screen.fill('lightblue')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet_group.add(player.create_bullet())

    player_group.update()
    bullet_group.update()

    player_group.draw(screen)
    bullet_group.draw(screen)
    pygame.display.update()
    clock.tick(60)