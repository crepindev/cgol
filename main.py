import pygame as pg
import sys

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
BLOCK_SIZE = 20


def main():
    global SCREEN, CLOCK
    pg.init()
    SCREEN = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pg.time.Clock()
    SCREEN.fill(WHITE)
    alive_cells = []
    dead_cells = []

    while True:
        cells = drawGrid()
        dead_cells.extend(cells)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                for cell in cells:
                    if cell.collidepoint(pos):
                        x = cell.center[0] // BLOCK_SIZE
                        y = cell.center[1] // BLOCK_SIZE
                        cell_pos = (x, y)
                        print(cell_pos)
                        if cell not in alive_cells:
                            alive_cells.append(cell)
                        elif cell in alive_cells:
                            alive_cells.remove(cell)
                for cell in alive_cells:
                    pg.draw.rect(SCREEN, BLACK, cell, 0)

        pg.display.update()


def drawGrid():
    cells = []
    for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
            rect = pg.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pg.draw.rect(SCREEN, BLACK, rect, 1)
            cells.append(rect)
    return cells
            
            
if __name__ == "__main__":     
    main()