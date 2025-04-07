import pygame, sys, math

class Button():
    def __init__(self,name,startpos=[0,0], scale=1):
        if len(name)<=27-12:
            font=pygame.font.Font(None,125)
        elif len(name)<=31-12:
            font=pygame.font.Font(None,100)
        else:
            font=pygame.font.Font(None,60)
        self.name = name
        
       
        
        self.normalImage = pygame.image.load("Art/Button/Button.png")
        self.rect = self.normalImage.get_rect(center=startpos)
        text=font.render(name,True,pygame.Color(0,0,0))
        textPos = text.get_rect(center = [self.rect.width/2,self.rect.height/2])
        self.normalImage.blit(text,textPos)
        self.normalImage=pygame.transform.scale(self.normalImage,[self.rect.width*scale,self.rect.height*scale])

        
        self.hoverImage = pygame.image.load("Art/Button/Button Hover.png")
        self.rect = self.hoverImage.get_rect(center=startpos)
        text=font.render(name,True,pygame.Color(0,0,0))
        textPos = text.get_rect(center = [self.rect.width/2,self.rect.height/2])
        self.hoverImage.blit(text,textPos)
        self.hoverImage=pygame.transform.scale(self.hoverImage,[self.rect.width*scale,self.rect.height*scale])

        
        self.clickImage = pygame.image.load("Art/Button/Button while clicked.png")
        self.rect = self.clickImage.get_rect(center=startpos)
        text=font.render(name,False,pygame.Color(0,0,0))
        textPos = text.get_rect(center = [self.rect.width/2,self.rect.height/2])
        self.clickImage.blit(text,textPos)
        self.clickImage=pygame.transform.scale(self.clickImage,[self.rect.width*scale,self.rect.height*scale])

        self.image = self.normalImage
        self.rect = self.image.get_rect(center=startpos)
        
        
    def collidePoint(self, pt, isClicked):
        if pt[0] > self.rect.left and pt[0] < self.rect.right:
            if pt[1] > self.rect.top and pt[1] < self.rect.bottom:
                if isClicked:
                    self.image = self.clickImage
                else:
                    self.image = self.hoverImage
                self.rect = self.image.get_rect(center=self.rect.center)
                return True
        self.image = self.normalImage
        self.rect = self.image.get_rect(center=self.rect.center)
        return False
                    
        
    
