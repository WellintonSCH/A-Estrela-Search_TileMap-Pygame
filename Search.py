import time
import pygame
import networkx as nx
from GameControl import CoastControl

class Grafo():

    #Estrutura grafo

    def __init__(self, level, screen): 
        self.matriz = level
        self.num_linhas = len(level)
        self.num_colunas = len(level[0])
        self.vertices = {(i, j) for i in range(self.num_linhas) for j in range(self.num_colunas)}
        self.arestas = {}
        self.screen = screen

        for i in range(self.num_linhas):
            for j in range(self.num_colunas):
                if self.matriz[i][j] != 4:
                    vizinhos = self.obter_vizinhos(i, j)
                    for vizinho in vizinhos:
                        
                        peso = CoastControl(vizinho[0], vizinho[1])
                        if (i, j) not in self.arestas:
                            self.arestas[(i, j)] = []
                        self.arestas[(i, j)].append((vizinho, peso))


    def obter_vizinhos(self, i, j):
        vizinhos = []
        if i > 0 and self.matriz[i - 1][j] != 4:
            vizinhos.append((i - 1, j))
        if i < self.num_linhas - 1 and self.matriz[i + 1][j] != 4:
            vizinhos.append((i + 1, j))
        if j > 0 and self.matriz[i][j - 1] != 4:
            vizinhos.append((i, j - 1))
        if j < self.num_colunas - 1 and self.matriz[i][j + 1] != 4:
            vizinhos.append((i, j + 1))
        return vizinhos
    

    def SearchWin(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if self.matriz[i][j] == 6:
                    return(i, j)



    def criar_grafo_networkx(self):
        G = nx.Graph()

        for vertice in self.vertices:
            G.add_node(vertice)

        for vertice, vizinhos_pesos in self.arestas.items():
            for vizinho, peso in vizinhos_pesos:
                G.add_edge(vertice, vizinho, weight=peso)
        return G


    def encontrar_caminho_a_star(self, ponto_inicial):
        grafo_networkx = self.criar_grafo_networkx()
        ponto_destino = self.SearchWin()
        
        try:
            caminho = nx.astar_path(grafo_networkx, ponto_inicial, ponto_destino, self.Manhattan, weight='weight')
            return caminho
        except:
            WHITE = (255, 255, 255)
            self.screen.fill(WHITE)
            error_message = "Impossível chegar ao destino"
            font = pygame.font.Font(None, 26)
            text = font.render(error_message, True, (0,0,0))
            
            text_rect = text.get_rect(center=(310 // 2, 310 // 2))
            self.screen.blit(text, text_rect)
            pygame.display.flip()
            time.sleep(10)
        
        

    def Euclidean(self, atual, destino):
        return pow(pow(atual[0] - destino[0], 2) + pow(atual[1] - destino[1], 2), 1/2) #Distancia euclidiana

    

    def Manhattan(self, atual, destino):
        
        valor = abs(atual[0] - destino[0]) + abs(atual[1] - destino[1])
        peso = CoastControl(atual[0], atual[1])
        
        font = pygame.font.Font(None, 12)
        text = font.render(str(peso+valor), True, (255, 255, 255))

        text_rect = text.get_rect()
        text_rect.topleft = ((atual[0] * 31) + 20, (atual[1] * 31)+20)
        self.screen.blit(text, text_rect)

        #Monitorando o algoritimo a* pela função euristica  
        pygame.draw.circle(self.screen, (255,0,0), ((atual[0] * 31)+15, (atual[1] * 31)+15), 4)
        pygame.display.flip()
        time.sleep(0.2)
        
        print(f"Posição( {atual[0]}, {atual[1]} ): Heuristica = {valor}, Peso = {CoastControl(atual[0], atual[1])}")
        return valor
    

    def imprimir_grafo(self):
        for vertice in self.vertices:
            print(f"Vértice {vertice}:")
            if vertice in self.arestas:
                for vizinho, peso in self.arestas[vertice]:
                    print(f"  -> Vizinho: {vizinho}, Peso: {peso}")
