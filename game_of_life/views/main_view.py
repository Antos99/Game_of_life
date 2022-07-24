from .abstract_view import AbstractView
import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


class MainView(AbstractView):
    def __init__(self, name, model, height, width):
        super().__init__(name, model)
        self._window_height = height
        self._window_width = width
        self._screen = pygame.display.set_mode((width, height))
        self._clock = pygame.time.Clock()
        self._screen.fill(BLACK)
        self._grid = []

    def add_component(self, comp):
        pass

    def update(self, *args, **kwargs):
        self._grid = args[0]

    def show(self):
        self.model.notify()
        # Set the size of the cell
        cell_size = max(self._window_width, self._window_width) // max(len(self._grid), len(self._grid[0]))
        # Draw cells
        for x in range(0, len(self._grid)):
            for y in range(0, len(self._grid[x])):
                rect = pygame.Rect(cell_size*x, cell_size*y, cell_size, cell_size)
                if self._grid[x][y].status == 'Dead':
                    pygame.draw.rect(self._screen, BLACK, rect)
                else:
                    pygame.draw.rect(self._screen, GREEN, rect)
                pygame.draw.rect(self._screen, WHITE, rect, 1)

        pygame.display.flip()
