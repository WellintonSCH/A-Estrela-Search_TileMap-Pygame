import pygame
from level import level
from Map import Map
from Player import Player
from Search import Grafo


pygame.init()

amount_row = len(level)
amount_col = len(level[0])
size_block = 31


screen = pygame.display.set_mode((amount_row*size_block, amount_col*size_block))
clock = pygame.time.Clock()
running = True
dt = 0


map = Map()
player = Player(0, 0)

#Buscando e exibindo caminho no terminal
grafo = Grafo(level, screen)
grafo.imprimir_grafo()
caminho = grafo.encontrar_caminho_a_star((player.row, player.col))
print("\nCaminho ideal: ", caminho)
i = 0

while running:

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    map.Render(screen)
    player.Render(screen)


    # player.Update() # Ter o controle o Player
    player.MovTo(caminho[i]) # Algoritimo joga


    pygame.display.flip()
    dt = clock.tick(1) # 1 para ver  o algoritimo e 10 para jogar
    i+=1


    #Vitoria
    if level[player.row][player.col] == 6:
        running = False

pygame.quit()

print("Custo final", player.game_control.coast)
print("Pontos", player.game_control.points)
