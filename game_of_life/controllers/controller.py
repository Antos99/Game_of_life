from .abstract_controller import AbstractController
import pygame
import sys


class Controller(AbstractController):
    def __init__(self, model=None, view=None):
        super().__init__(model, view)

    def get_user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.model.cycle.cancel()
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.model.modify()
