import pygame
import random

class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if random.choice('12')=='1':
            self.image = pygame.image.load('images/pipes/double_pipe_1.png').convert_alpha()
        else:
            self.image = pygame.image.load('images/pipes/double_pipe_2.png').convert_alpha()
        self.rect = self.image.get_rect()

    def rotate(self,angle):
        rotImage = pygame.transform.rotozoom(self.image,angle,1)
        w,h = rotImage.get_size()
        new_pos = (640 - w/2, 360 - h/2)
        return rotImage,new_pos
