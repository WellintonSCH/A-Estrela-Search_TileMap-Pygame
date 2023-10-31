import pygame
import networkx as nx
from GameControl import CoastControl

class Grafo():

    #Estrutura grafo

    def __init__(self, level, screen): 
        
        G = nx.Graph()

        self.level = level
        self.row_count = len(level)
        self.col_count = len(level[0])

        self.node_list_position = {(i, j) for i in range(self.row_count) for j in range(self.col_count) if self.level[i][j] != 4}
        self.edges_list_position = {} # arestas
        
        self.screen = screen

        for i in range(self.row_count):
            for j in range(self.col_count):
                if self.level[i][j] != 4:
                    edges_position = self.find_edges(i, j)
                    for edge in edges_position:
                        
                        weight = CoastControl(edge[0], edge[1])
                        if (i, j) not in self.edges_list_position:
                            self.edges_list_position[(i, j)] = []
                        self.edges_list_position[(i, j)].append((edge, weight))


    def find_edges(self, i, j):
        list_edges = []
        if i > 0 and self.level[i - 1][j] != 4: # cima
            list_edges.append((i - 1, j))

        if i < self.row_count - 1 and self.level[i + 1][j] != 4: # baixo
            list_edges.append((i + 1, j))

        if j > 0 and self.level[i][j - 1] != 4: # esquerda
            list_edges.append((i, j - 1))

        if j < self.col_count - 1 and self.level[i][j + 1] != 4: # direita
            list_edges.append((i, j + 1))
        return list_edges
    

            # [1,1,1]
            # [1,1,1]
            # [1,1,1]
    

    def SearchWin(self):
        for i in range(len(self.level)):
            for j in range(len(self.level[i])):
                if self.level[i][j] == 6:
                    return(i, j)


    def MakeGraphNetwokX(self):
        G = nx.Graph()

        for node_position in self.node_list_position:
            G.add_node(node_position)

        for node_position, weight_edge in self.edges_list_position.items():
            for edge, weight in weight_edge:
                G.add_edge(node_position, edge, weight=weight)
        return G


    def FindPathAStar(self, start_point):
        graph_networkx = self.MakeGraphNetwokX()
        end_point = self.SearchWin()
        
        try:
            path = nx.astar_path(graph_networkx, start_point, end_point, self.Manhattan, weight='weight')
        except:
            raise Exception("Caminho não encontrado.")
        return path


    def Euclidean(self, position, destin):
        return pow(pow(position[0] - destin[0], 2) + pow(position[1] - destin[1], 2), 1/2) #Distancia euclidiana

    
    def Manhattan(self, position, destin):

        #Exibir calculo das informações nós visitados na tela
        self.PositionMonitor(position, destin, 100)

        return abs(position[0] - destin[0]) + abs(position[1] - destin[1])
    
    
    def PositionMonitor(self, position, destin, delay):
        
        if self.level[position[0]][position[1]] != 4:
            
            h = abs(position[0] - destin[0]) + abs(position[1] - destin[1])
            g = CoastControl(position[0], position[1])
            f = g + h

            font = pygame.font.Font(None, 12)
            text = font.render(str(f), True, (255, 255, 255))

            text_rect = text.get_rect()
            text_rect.topleft = ((position[0] * 31) + 20, (position[1] * 31)+20)
            self.screen.blit(text, text_rect)

            pygame.draw.circle(self.screen, (255,0,0), ((position[0] * 31)+15, (position[1] * 31)+15), 4)
            pygame.display.flip()
            pygame.time.delay(delay)
            print(f"Posição( {position[0]}, {position[1]} ): Heuristica = {h}, Peso = {CoastControl(position[0], position[1])}")


    def print_grafo(self):
        for node_position in self.node_list_position:
            print(f"Vértice {node_position}:")
            if node_position in self.edges_list_position:
                for edge_position, weight in self.edges_list_position[node_position]:
                    print(f"  -> Vizinho: {edge_position}, Peso: {weight}")