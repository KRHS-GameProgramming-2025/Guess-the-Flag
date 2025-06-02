

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
clicked = False

oPressed = False
mPressed = False
nPressed = False
iPressed = False
omni = False

def getFlags(kind):
    path = "Art/" + kind.replace(" ", "")
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


mode="Start"
Version=""

while True:
    bgimage=pygame.image.load("Art/Screens/flagger.png")
    bgrect=bgimage.get_rect()
    buttons = [Button("State Flags",[968/4,200], .5),
               Button("America Flags",[968/4, 300], .5),
               Button("Europe Flags",[968/4,400], .5),
               Button("WWII Flags", [968/4, 500], .5),
               Button("USSR Flags",[968/4, 600], .5),
               
               Button("Asia Flags",[968/4*3, 200], .5),
               Button("Africa Flags", [968/4*3,300], .5),
               Button("Oceania Flags",[968/4*3,400], .5),
               Button("WWI Flags",[968/4*3,500], .5),
               Button("Organization Flags",[968/4*3,600], .5),
               Button("China Flags",[968/4*3,700], .5),
            
               Button("Credits", [968/4, 950],.5)
               ]
    pygame.mixer.music.load("Sound/Quirky Dog.mp3")
    pygame.mixer.music.set_volume(5)
    pygame.mixer.music.play() 
    while mode =="Start":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
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
                            if button.name == "Credits":
                                mode = "Credits"
                            else:
                                Version = button.name
                                mode = "Play"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o and not oPressed and not mPressed and not nPressed and not iPressed:
                    oPressed = True
                elif event.key == pygame.K_m and oPressed and not mPressed and not nPressed and not iPressed:
                    mPressed = True
                elif event.key == pygame.K_n and oPressed and mPressed and not nPressed and not iPressed:
                    nPressed = True
                elif event.key == pygame.K_i and oPressed and mPressed and nPressed and not iPressed:
                    iPressed = True
                    
                else:
                    oPressed = False
                    mPressed = False
                    nPressed = False
                    iPressed = False
                    
        if oPressed and mPressed and nPressed and iPressed:
            print("WHERE IS OMNI_MAN!!!!")
            if not omni: buttons+=[Button("Invincible",[968/4*3,600], .5)]
            omni=True
            oPressed = False
            mPressed = False
            nPressed = False
            iPressed = False
                    
        
        screen.fill((181, 181, 181))  
        screen.blit(bgimage,bgrect)
        for button in buttons:
            screen.blit(button.image, button.rect)
        pygame.display.flip()
        clock.tick(60)
    
    if mode != "Credits":   
        flags = getFlags(Version)                                                                                
        random.shuffle(flags)
        flagNames = []
        for flag in flags:
            flagNames += [flag.name]                                                                              
                  

        s=0
        flag = flags[s]
        buttons=buildButtons(flag.name, flags)
        buttons+= [Button("Back", [size[0]/6, 950], .5)]
        
        points = 0
        score = Hud("Score: ", points, "right", [0,0])
        progress = Hud ("/"+str(len(flags)), s, "left", [968,0])

    while mode =="Play":
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
                            elif button.name == "Back":
                                mode="Start"
                                break
                            else:
                                wrong.play()
                            s+=1
                            progress.update(s)
                            try:
                                flag = flags[s] 
                                buttons=buildButtons(flag.name, flags)
                                buttons+= [Button("Back", [size[0]/6, 950], .5)]
                            except:
                                if points/len(flags) > winThreshold:
                                    print("Winner")
                                    win.play()
                                    mode = "Win"
                                else:
                                    lose.play()
                                    print("lose")
                                    mode = "Lose"

        screen.fill((181, 181, 181))  
        screen.blit(flag.image,flag.rect)
        for button in buttons:
            screen.blit(button.image, button.rect)
        screen.blit(score.image, score.rect)
        screen.blit(progress.image, progress.rect)
        pygame.display.flip()
        clock.tick(60)
        
    bgimage=pygame.image.load("Art/Screens/YOU WIN.png")
    bgrect=bgimage.get_rect()
    buttons = [Button("Play Again",[968/2,800], .5)]
    
    while mode =="Win":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
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
                            mode = "Start"
        
        screen.fill((181, 181, 181))  
        screen.blit(bgimage,bgrect)
        for button in buttons:
            screen.blit(button.image, button.rect)
        pygame.display.flip()
        clock.tick(60)
    
    bgimage=pygame.image.load("Art/Screens/YOU LOST.png")
    bgrect=bgimage.get_rect()
    buttons = [Button("Play Again",[968/2,800], .5)]
    
    while mode =="Lose":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
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
                            mode = "Start"
        
        screen.fill((181, 181, 181))  
        screen.blit(bgimage,bgrect)
        for button in buttons:
            screen.blit(button.image, button.rect)
        pygame.display.flip()
        clock.tick(60)
        
    bgimage=pygame.image.load("Art/Screens/Credits.png")
    bgrect=bgimage.get_rect()
    buttons = [Button("Menu",[968/2,875], .5)]
    
    while mode =="Credits":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
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
                            mode = "Start"
        
        screen.fill((181, 181, 181))  
        screen.blit(bgimage,bgrect)
        for button in buttons:
            screen.blit(button.image, button.rect)
        pygame.display.flip()
        clock.tick(60)
        
