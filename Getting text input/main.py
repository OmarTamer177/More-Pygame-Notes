######################################################################
# Getting text input
#
# 1.Create text font
# 2.Get user input and render it
# 3.blit text on screen
######################################################################
import pygame, sys

pygame.init()

screen = pygame.display.set_mode((800, 800)) 
clock = pygame.time.Clock()

#create basic font
base_font = pygame.font.Font(None, 25)
user_text = ''

#create text surface and rectangle
text_surface = base_font.render(user_text, True, 'white')
text_rect = pygame.Rect(200,200,140,32)

#The color of the text-box is initially grey
#When the user press on the text box it changes to white
color_active = 'white'
color_passive = 'grey15'
color = color_passive

#A flag indicating if the text-box is ready to be written in
text_active = False

while True:
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if text_rect.collidepoint(event.pos):
                text_active = True
            else:
                text_active = False

        #if the user typed in the text box while the it is active, it types normally
        #if not; it doesn't type
        if event.type == pygame.KEYDOWN:
            if text_active:
                #handling deleting with backspace 
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                #handling the max size of the text-box
                elif text_surface.get_width() < 200:
                    user_text += event.unicode

    text_surface = base_font.render(user_text, True, 'white')

    #change the color of the text-box depending on its state
    if text_active:
        color = color_active
    else:
        color = color_passive

    pygame.draw.rect(screen, color, text_rect, 2)
    screen.blit(text_surface, (text_rect.x + 5, text_rect.y + 5))

    text_rect.width = max(100, text_surface.get_width() + 10)

    pygame.display.update()
    clock.tick(240)