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

def buildButtons(answer,flaglist):
    correct = random.randint(0,3)
    locations = [[size[0]/4,750],
                 [size[0]/4,850],
                 [size[0]/4*3,750],
                 [size[0]/4*3,850]]
    buttons = []
    buttonTexts = [answer]
    for i, button in enumerate(range(4)):
        if i == correct:
            buttons += [Button(answer, locations[i],.5)]
        else:
            text = answer
            while text in buttonTexts:
                num = random.randint(0, len(flaglist))
                text = flaglist[num].name
            buttonTexts += [text]
            buttons += [Button(text, locations[i],.5)]
    return buttons

flags = getFlags("State Flags")                                                                                
random.shuffle(flags)
flagNames = []
for flag in flags:
    flagNames += [flag.name]                                                                              
          

s=0
flag = flags[s]
buttons=buildButtons(flag.name, flags)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                s+=1
                try:
                    flag = flags[s] 
                    buttons=buildButtons(flag.name, flags)
                except:
                    s=0
            if event.key == pygame.K_LEFT:
                s-=1
                try:
                    flag = flags[s]
                    buttons=buildButtons(flag.name, flags)
                except:
                    s= len(flags)-1
            
            
    
    
    screen.fill((181, 181, 181))  
    screen.blit(flag.image,flag.rect)
    for button in buttons:
        screen.blit(button.image, button.rect)
    pygame.display.flip()
    clock.tick(60)
