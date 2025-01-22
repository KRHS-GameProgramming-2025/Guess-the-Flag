import pygame, sys, math

class StateFlag():
    def __init__(self,name,startpos=[0,0], size=[1024, 900]):
        self.image = pygame.image.load("Art/StateFlags/Flag_of_"+ name+".png")
        self.image=pygame.transform.scale(self.image,size)
        self.rect = self.image.get_rect(center=startpos)
