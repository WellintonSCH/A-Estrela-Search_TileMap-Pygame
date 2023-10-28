from level import level

class GameControl():
    

    def __init__(self):
        self.points = 0
        self.coast = 0
    

    def GameControl(self, row, col):

        self.Flowers(row, col)
        self.coast += CoastControl(row, col)


    def Flowers(self, row, col):
        if level[row][col] == 5:
            self.points += 1
            level[row][col] = 0 #Coleta
        

def CoastControl(row, col):
    
    if level[row][col] == 0:
        return int(1)
    elif level[row][col] == 1:
        return int(4)
    elif level[row][col] == 2:
        return int(10)
    elif level[row][col] == 3:
        return int(20)
    elif level[row][col] == 4:
        return int(100)
    elif level[row][col] == 5:
        return int(0)
    else: return 0