import pygame, sys, math, random
from FlagDisplay import*
pygame.init()

clock = pygame.time.Clock();
size = [1224, 1000]
screen = pygame.display.set_mode(size)

flag = StateFlag("New_Hampshire", [612,500])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
    
    
    screen.fill((181, 181, 181))  
    
    pygame.display.flip()
    clock.tick(60)
    print(clock.get_fps() )
