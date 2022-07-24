from abc import ABC, abstractmethod


class AbstractApp(ABC):
    def __init__(self, controller):
        super().__init__()
        self.__controller = controller

    @abstractmethod
    def run_app(self):
        pass

    @property
    def controller(self):
        return self.__controller

    @controller.setter
    def controller(self, new_controller):
        self.__controller = new_controller
