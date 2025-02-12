import pygame, sys, math, random, os
from FlagDisplay import*
from Button import*
pygame.init()

clock = pygame.time.Clock();
size = [968, 1000]
screen = pygame.display.set_mode(size)

def getFlags(kind):
    if kind == "State Flags":
        path = "Art/StateFlags"
    elif kind == "Europe Flags":
        path = "Art/EuropeFlags"
    files = os.listdir(path)
    
    flags = []
    for f in files:
        if f[-4:] == ".png":
            flags += [Flag(path, f[8:-4], [size[0]/2,50], .75)]
    return flags
    

flags = getFlags("Europe Flags")                                                                                
                                                                                
          

s=0
flag = flags[s]
button1=Button(flags[s].name, [size[0]/4,750],.5)
button2=Button(flags[s].name, [size[0]/4,850],.5)
button3=Button(flags[s].name, [size[0]/4*3,750],.5)
button4=Button(flags[s].name, [size[0]/4*3,850],.5)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                s+=1
                try:
                    flag = flags[s] 
                    button1=Button(flags[s].name, [size[0]/4,750],.5)
                    button2=Button(flags[s].name, [size[0]/4,850],.5)
                    button3=Button(flags[s].name, [size[0]/4*3,750],.5)
                    button4=Button(flags[s].name, [size[0]/4*3,850],.5)
                except:
                    s=0
            if event.key == pygame.K_LEFT:
                s-=1
                try:
                    flag = flags[s]
                    button1=Button(flags[s].name, [size[0]/4,750],.5)
                    button2=Button(flags[s].name, [size[0]/4,850],.5)
                    button3=Button(flags[s].name, [size[0]/4*3,750],.5)
                    button4=Button(flags[s].name, [size[0]/4*3,850],.5)
                except:
                    s= len(flags)-1
            
            
    
    
    screen.fill((181, 181, 181))  
    screen.blit(flag.image,flag.rect)
    screen.blit(button1.image,button1.rect)
    screen.blit(button2.image,button2.rect)
    screen.blit(button3.image,button3.rect)
    screen.blit(button4.image,button4.rect)
    pygame.display.flip()
    clock.tick(60)
