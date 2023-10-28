import pygame
from level import level

class Map():
    def __init__(self):

        self.FULL_IMAGE = pygame.image.load('img/terrain.png')
        self.BLOCK_SIZE = 31
        
        self.block_images = {
            0: self.FULL_IMAGE.subsurface(pygame.Rect(0, 352, self.BLOCK_SIZE, self.BLOCK_SIZE)),    # grama
            1: self.FULL_IMAGE.subsurface(pygame.Rect(576, 352, self.BLOCK_SIZE, self.BLOCK_SIZE)),  # areia
            2: self.FULL_IMAGE.subsurface(pygame.Rect(384, 160, self.BLOCK_SIZE, self.BLOCK_SIZE)),  # pedra
            3: self.FULL_IMAGE.subsurface(pygame.Rect(288, 352, self.BLOCK_SIZE, self.BLOCK_SIZE)),  # pantano
            4: self.FULL_IMAGE.subsurface(pygame.Rect(864, 160, self.BLOCK_SIZE, self.BLOCK_SIZE)),  # agua
            5: self.FULL_IMAGE.subsurface(pygame.Rect(98, 352, self.BLOCK_SIZE, self.BLOCK_SIZE)),  # pontos
            6: self.FULL_IMAGE.subsurface(pygame.Rect(416, 608, self.BLOCK_SIZE, self.BLOCK_SIZE)),  # chegada
        }

    def Render(self, screen):

        for row in range(len(level)):
            for col in range(len(level[row])):
                block = self.block_images[level[row][col]]
                screen.blit(block, (col * self.BLOCK_SIZE, row * self.BLOCK_SIZE))
    