import pygame
from level import level
from Map import Map
from Player import Player
from Search import Grafo

def menu(screen):
    font = pygame.font.Font(None, 36)
    options = ["Play", "aStar", "Sair"]
    current_option = 0
    texts = [font.render(option, 1, (255, 255, 255)) for option in options]
    text_positions = [text.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()/2 + i*40) for i, text in enumerate(texts)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    current_option = (current_option + 1) % len(options)
                elif event.key == pygame.K_UP:
                    current_option = (current_option - 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    screen.fill((0, 0, 0))
                    return current_option

        screen.fill((0, 0, 0))
        for i, text in enumerate(texts):
            option_rect = text_positions[i]
            if i == current_option:
                pygame.draw.rect(screen, (255, 255, 255), option_rect, 2)  # Destacar a opção selecionada
            screen.blit(text, text_positions[i])

        pygame.display.flip()


pygame.init()


#Quantidade de linhas e colunas da matriz level * tamanho em pixel do sprite = tamanho da tela
amount_row = len(level)
amount_col = len(level[0])
size_block = 31

#pygame
screen = pygame.display.set_mode((amount_col*size_block, amount_row*size_block))
clock = pygame.time.Clock()
running = True
dt = 0

option = menu(screen)

map = Map()
player = Player(0, 0)

if option == 0:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            map.Render(screen)
            player.Render(screen)
            player.Update()  # Ter o controle o Player
            
            pygame.display.flip()
            dt = clock.tick(60)

            #Vitoria
            if level[player.row][player.col] == 6:
                running = False

# Opção 2: aStar
elif option == 1:

    #Exibindo mapa para visualização
    map.Render(screen)


    #Criando objeto grafo personalizado
    grafo = Grafo(level, screen)
    grafo.print_grafo()

    #Buscando e exibindo caminho no terminal
    try:
        caminho = grafo.FindPathAStar((player.row, player.col))
    except:
        screen.fill((0,0,0))
        error_message = "Impossível chegar ao destino"
        font = pygame.font.Font(None, 26)
        text = font.render(error_message, True, (255, 255, 255))
        
        text_rect = text.get_rect(center=(310 // 2, 310 // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(1000)
        pygame.quit()
        quit()

    print("\nCaminho ideal: ", caminho)
    
    i = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        map.Render(screen)
        player.Render(screen)
        player.MovTo(caminho[i])  # Algoritmo joga
        
        
        pygame.display.flip()
        dt = clock.tick(60) # 1 para ver  o algoritimo e 10 para jogar
        i+=1

        #Vitoria
        if level[player.row][player.col] == 6:
            running = False

# Opção 3: Sair
elif option == 2:
    pygame.quit()
    quit()



print("Custo final", player.game_control.coast)
print("Pontos", player.game_control.points)
