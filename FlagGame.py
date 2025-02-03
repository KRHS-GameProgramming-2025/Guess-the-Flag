import pygame, sys, math, random
from FlagDisplay import*
from Button import*
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
          "Florida",
          "Georgia",
          "Hawaii",
          "Idaho",
          "Illinois",
          "Indiana",
          "Iowa",
          "Kansas",
          "Kentucky",
          "Louisiana",
          "Maine",
          "Maryland",
          "Massachusetts",
          "Michigan",
          "Minnesota",
          "Mississippi",
          "Missouri",
          "Montana",
          "Nebraska",
          "Nevada",
          "New_Hampshire",
          "New_Jersey",
          "New_Mexico",
          "New_York",
          "North_Carolina",
          "North_Dakota",
          "Ohio",
          "Oklahoma",
          "Oregon",
          "Pennsylvania",
          "Rhode_Island",
          "South_Carolina",
          "South_Dakota",
          "Tennessee",
          "Texas",
          "Utah",
          "Vermont",
          "Virginia",
          "Washington",
          "West_Virginia",
          "Wisconsin",
          "Wyoming"]
                                                                                         
          

s=0
flag = StateFlag(states[s], [size[0]/2,50],.75)
button1=Button(states[s], [size[0]/4,750],.5)
button2=Button(states[s], [size[0]/4,850],.5)
button3=Button(states[s], [size[0]/4*3,750],.5)
button4=Button(states[s], [size[0]/4*3,850],.5)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                s+=1
                try:
                    flag = StateFlag(states[s], [size[0]/2,50],.75)
                    button1=Button(states[s], [size[0]/4,750],.5)
                    button2=Button(states[s], [size[0]/4,850],.5)
                    button3=Button(states[s], [size[0]/4*3,750],.5)
                    button4=Button(states[s], [size[0]/4*3,850],.5)
                except:
                    s-=1
            if event.key == pygame.K_LEFT:
                s-=1
                try:
                    flag = StateFlag(states[s], [size[0]/2,50],.75)
                    button1=Button(states[s], [size[0]/4,750],.5)
                    button2=Button(states[s], [size[0]/4,850],.5)
                    button3=Button(states[s], [size[0]/4*3,750],.5)
                    button4=Button(states[s], [size[0]/4*3,850],.5)
                except:
                    s+=1
            
            
    
    
    screen.fill((181, 181, 181))  
    screen.blit(flag.image,flag.rect)
    screen.blit(button1.image,button1.rect)
    screen.blit(button2.image,button2.rect)
    screen.blit(button3.image,button3.rect)
    screen.blit(button4.image,button4.rect)
    pygame.display.flip()
    clock.tick(60)
