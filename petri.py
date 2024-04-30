import numpy as np

def init_petri(shape, init):
    # takes 'shape' as int or tuple of ints to size matrix, and
    # 'init' as list of tuples with (x,y) coordinates of alive cells
    # returns matrix of cells i.e. the 'petri dish'
    petri = np.zeros(shape, dtype=int)
    for cell in init:
        x = cell[0]
        y = cell[1]
        petri[x][y] = 1
    return petri

#test
shape = (3,3)
init = [(1,1)]
print(init_petri(shape, init))