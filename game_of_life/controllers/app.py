from .abstract_app import AbstractApp
from ..models.board_model import BoardModel
from ..views.main_view import MainView
import pygame


class App(AbstractApp):
    def __init__(self, controller, window_height, window_width, rows, columns, period):
        super().__init__(controller)
        pygame.init()

        self._model = BoardModel(rows, columns, period)
        self._view = MainView('MainView', self._model, window_height, window_width)
        self._model.add_observer(self._view)

        controller.model = self._model
        controller.view = self._view

    def run_app(self):
        while True:
            self.controller.get_user_input()
            self.controller.view.show()
