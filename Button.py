import pygame, sys, math

class Button():
    def __init__(self,name,startpos=[0,0], scale=1):
        self.image = pygame.image.load("Art/button.png")
        self.rect = self.image.get_rect(center=startpos)
        
        font=pygame.font.Font(None,125)
        text=font.render(name,False,pygame.Color(0,0,0,255))
        textPos = text.get_rect(center = [self.rect.width/2,self.rect.height/2])
        self.image.blit(text,textPos)
        self.rect = self.image.get_rect(center=startpos)
        
        
        
        self.image=pygame.transform.scale(self.image,[self.rect.width*scale,self.rect.height*scale])
        self.rect = self.image.get_rect(center=startpos)
        
