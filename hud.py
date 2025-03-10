import pygame, sys, math

class Hud():
    def __init__ (self,baseText,startVal=0, side="right", startPos=[0,0]):
        self.font = pygame.font.Font(None, 46)
        self.baseText = baseText
        self.side = side
        if side == "right":
            self.image = self.font.render(self.baseText + str(startVal), 1, (255,255,255))
            self.rect = self.image.get_rect(topleft = startPos)
        else:
            self.image = self.font.render(str(startVal) + self.baseText, 1, (255,255,255))
            self.rect = self.image.get_rect(topright = startPos)
        
        
        
    def update(self, score):
        if self.side == "right":
            text = self.baseText + str(score)
            self.image =  self.font.render(text, 1, (255,255,255))
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        else:
            text = str(score) + self.baseText
            self.image =  self.font.render(text, 1, (255,255,255))
            self.rect = self.image.get_rect(topright = self.rect.topright)
            
            
