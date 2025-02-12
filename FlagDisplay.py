import pygame, sys, math

class Flag():
    def __init__(self,path, name,startpos=[0,0], scale=1):
        self.image = pygame.image.load(path+"/Flag_of_"+ name+".png")
        self.rect = self.image.get_rect(midtop=startpos)
        self.name = name.replace("_", " ")
        
        self.image=pygame.transform.scale(self.image,[self.rect.width*scale,self.rect.height*scale])
        self.rect = self.image.get_rect(midtop=startpos)
