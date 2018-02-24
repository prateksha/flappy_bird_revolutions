import pygame
import math

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/fat_bird.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = None
