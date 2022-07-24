from abc import ABC, abstractmethod


class AbstractView(ABC):
    def __init__(self, name, model):
        super().__init__()
        self.__name = name
        self.__component_list = dict()
        self.__model = model

    @property
    def name(self):
        return self.__name

    @property
    def model(self):
        return self.__model

    def get_children(self):
        return self.__component_list.values()

    def remove_component(self, name):
        if name in self.__component_list:
            del self.__component_list[name]

    @abstractmethod
    def add_component(self, comp):
        if comp.name not in self.__component_list:
            self.__component_list[comp.name] = comp

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @abstractmethod
    def show(self):
        pass
