##########################################################################################
# Simulating physics(pymunk)
#
# Pymunk: A 2d physics engine that is independant from other libraries, 
#         making physics calculations in a 2d space, and pygame will be 
#         used to visualize these calculations
#
# How pymunk works: creating a space where all calculations will take place,
#                   which is mostly gravity(also updating the space objects)  
#
# phisical objects:
#                -> Body: an atom that is affected by pyhsics
#                -> Shape: an area around the body that can collide
#
# Bodies:
#       -> static: doesn't move but other objects collide with it
#       -> dynamic: can be moved by physics 
#                   (it needs mass(weight), inertia(resistence to movement), body_type)
#       -> kinetic: can be moved by the player(or other non-physical code)
##########################################################################################
import pygame, sys
import pymunk

def create_apple(space, pos):
    #creating a dynamic body using Body(mass, inertia, body_type[dynamic, static, ....])
    body = pymunk.Body(1, 100, pymunk.Body.DYNAMIC)
    body.position = pos
    #creating a simplified shape around the apple
    shape = pymunk.Circle(body, 50)
    #add the object to space
    space.add(body, shape)

    #return the shape(its position) to visualize it with pygame
    return shape

#Takes a list of pymunk physical objects and draw it on pygame screen
def draw_apples(apples):
    for apple in apples:
        x = int(apple.body.position.x)
        y = int(apple.body.position.y)
        pygame.draw.circle(screen, 'red', (x, y), 50)

def static_body(space, pos):
    #creating a static body using Body(mass, inertia, body_type[dynamic, static, ....])
    body = pymunk.Body(1, 100, pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, 60)
    space.add(body, shape)

    return shape

#drawing static objects(similar to draw_apples())
def draw_static_body(static_bodies):
    for object in static_bodies:
        x = int(object.body.position.x)
        y = int(object.body.position.y)
        pygame.draw.circle(screen, 'black', (x, y), 60)

pygame.init()
screen = pygame.display.set_mode((800, 700))
clock = pygame.time.Clock()

#Creating a space that can calculate physics using pymunk
space = pymunk.Space()
#giving the space gravity(horizontal_gravity, vertical_gravity)
space.gravity = (0, 200)

apples = []
static_bodies = [static_body(space, (450, 500)), static_body(space, (200, 600))]

while True:
    screen.fill('grey')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #if mouse button was pressed, create an apple
        if event.type == pygame.MOUSEBUTTONDOWN:
            apples.append(create_apple(space, event.pos))

    draw_apples(apples)
    draw_static_body(static_bodies)

    #itirate over the objects and check for out of screen objects
    for index in range(len(apples) - 1, -1, -1):
        if apples[index].body.position.y > 1000:
            apples.pop(index)

    #how fast do we want to update the space
    space.step(1/50)
    pygame.display.update()
    clock.tick(120)
