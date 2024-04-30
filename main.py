import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
BLOCK_SIZE = 20


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)

    while True:
        cells = drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked_cell = [cell for cell in cells if cell.rect.collidepoint]
        pygame.display.update()


def drawGrid():
    cells = []
    for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)
            cells.append(rect)
    return cells
            
            
if __name__ == "__main__":     
    main()