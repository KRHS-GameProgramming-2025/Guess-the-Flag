import pygame, sys, math, random, os
from FlagDisplay import*
from Button import*
from hud import*
pygame.init()

clock = pygame.time.Clock();
size = [968, 1000]
screen = pygame.display.set_mode(size)

correct=pygame.mixer.Sound("Sound/Correct.mp3")
wrong=pygame.mixer.Sound("Sound/Wrong.mp3")
lose=pygame.mixer.Sound("Sound/Booooooooooo.mp3")
win=pygame.mixer.Sound("Sound/Winning Game.mp3")

winThreshold = .80

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
                num = random.randint(0, len(flaglist)-1)
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
clicked = False
points = 0
score = Hud("Score: ", points, "right", [0,0])
progress = Hud ("/"+str(len(flags)), s, "left", [968,0])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
        # ~ if event.type == pygame.KEYDOWN:
            # ~ if event.key == pygame.K_RIGHT:
                # ~ s+=1
                # ~ try:
                    # ~ flag = flags[s] 
                    # ~ buttons=buildButtons(flag.name, flags)
                # ~ except:
                    # ~ s=0
            # ~ if event.key == pygame.K_LEFT:
                # ~ s-=1
                # ~ try:
                    # ~ flag = flags[s]
                    # ~ buttons=buildButtons(flag.name, flags)
                # ~ except:
                    # ~ s= len(flags)-1
        if event.type == pygame.MOUSEMOTION:
            for button in buttons:
                button.collidePoint(event.pos, clicked)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicked = True
                for button in buttons:
                    button.collidePoint(event.pos, clicked)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clicked = False
                for button in buttons:
                    if button.collidePoint(event.pos, clicked):
                        if button.name == flag.name:
                            points += 1
                            score.update(points)
                            correct.play()
                        else:
                            wrong.play()
                        s+=1
                        progress.update(s)
                        try:
                            flag = flags[s] 
                            buttons=buildButtons(flag.name, flags)
                        except:
                            if points/len(flags) > winThreshold:
                                print("Winner")
                                win.play()
                            else:
                                lose.play()
                                print("lose")
                            
                
            
            
            
            
    
    
    screen.fill((181, 181, 181))  
    screen.blit(flag.image,flag.rect)
    for button in buttons:
        screen.blit(button.image, button.rect)
    screen.blit(score.image, score.rect)
    screen.blit(progress.image, progress.rect)
    pygame.display.flip()
    clock.tick(60)
