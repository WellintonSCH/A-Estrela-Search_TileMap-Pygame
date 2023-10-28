import pygame
from level import level
from GameControl import GameControl


class Player(pygame.sprite.Sprite):
    FULL_PLAYER_IMAGE = pygame.image.load('img/player.png')

    BLOCK_SIZE = 31

    def __init__(self, row, col):
        super().__init__()

        #Altura e largura
        self.PLAYER_WIDTH = 11
        self.PLAYER_HEIGTH = 16


        #Posição do sprite inicial em FULL_PLAYER_IMAGE
        self.img_X = 19
        self.img_Y = 0

        self.player_frame = self.FULL_PLAYER_IMAGE.subsurface(pygame.Rect(self.img_X, self.img_Y, self.PLAYER_WIDTH, self.PLAYER_HEIGTH))
        self.rect = self.player_frame.get_rect()

        #Centralizando o player em meio ao bloco
        self.rect.x = 10
        self.rect.y = 7
       
        #Posicionando o player
        self.row = row
        self.col = col

        #Inicializando gae control
        self.game_control = GameControl()
    

    def Update(self):
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.MovLeft()
        if keys[pygame.K_RIGHT]:
            self.MovRight()
        if keys[pygame.K_UP]:
            self.MovUp()
        if keys[pygame.K_DOWN]:
            self.MovDown()
    

    def Render(self, screen):
        self.player_frame = self.FULL_PLAYER_IMAGE.subsurface(pygame.Rect(self.img_X, self.img_Y, self.PLAYER_WIDTH, self.PLAYER_HEIGTH))
        self.player_frame.set_colorkey((0, 0, 0))
        screen.blit(self.player_frame, self.rect)

    
    def MovLeft(self):
        self.img_Y = 16
        if self.col - 1 >= 0:
            if level[self.row][self.col - 1] != 4:
                self.rect.x -= self.BLOCK_SIZE
                self.col -= 1
                self.game_control.GameControl(self.row, self.col)

    def MovRight(self):
        self.img_Y = 32
        if self.col + 1 < 10 :
            if level[self.row][self.col+1] != 4:
                self.col += 1
                self.rect.x += self.BLOCK_SIZE
                self.game_control.GameControl(self.row, self.col)


    def MovUp(self):
        self.img_Y = 48
        if self.row - 1 >= 0:
            if level[self.row - 1][self.col] != 4:
                self.rect.y -= self.BLOCK_SIZE
                self.row -= 1
                self.game_control.GameControl(self.row, self.col)


    def MovDown(self):
        self.img_Y = 0
        if self.row + 1 < 10:
            if level[self.row + 1][self.col] != 4:
                self.rect.y += self.BLOCK_SIZE
                self.row += 1
                self.game_control.GameControl(self.row, self.col)
    
    
    def MovTo(self, destin):

        if self.row - destin[0] == -1:
            self.MovDown()
        elif self.row - destin[0] == 1:
            self.MovUp()
        elif self.col - destin[1] == -1:
            self.MovRight()
        elif self.col - destin[1] == 1:
            self.MovLeft()

