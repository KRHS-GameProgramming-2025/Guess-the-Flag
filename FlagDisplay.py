import pygame, sys, math

class StateFlag():
    def __init__(self,name,startpos=[0,0], scale=1):
        self.image = pygame.image.load("Art/StateFlags/Flag_of_"+ name+".png")
        self.rect = self.image.get_rect(midtop=startpos)
        
        self.image=pygame.transform.scale(self.image,[self.rect.width*scale,self.rect.height*scale])
        self.rect = self.image.get_rect(midtop=startpos)
