import pygame, sys, math, random
from FlagDisplay import*
pygame.init()

clock = pygame.time.Clock();
size = [968, 1000]
screen = pygame.display.set_mode(size)

states = ["Alabama",
          "Alaska",
          "Arizona",
          "Arkansas",
          "California",
          "Colorado",
          "Connecticut",
          "Delaware",
          "Flordia",
          "Hawaii",
          "Idaho",
          "Illonois",
          "Indiana",
          "Iowa",
          "Kansas",
          "Kentucky",
          "Louisiana",
          "Maryland",
          "Massachusetts"
          "Michigan",
          "Minnesita",
          "Mississipi",
          "Montana",
          "Nebraska",
          "Nevada",
          "New_Hampshire",
          "New_Jersey",
          "New_Mexico",
          "New_York",
          


flag = StateFlag("Idaho", [size[0]/2,50],.75)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
    
    
    screen.fill((181, 181, 181))  
    screen.blit(flag.image,flag.rect)
    pygame.display.flip()
    clock.tick(60)
    print(clock.get_fps() )
