from .abstract_model import AbstractModel


class CellModel(AbstractModel):
    def __init__(self):
        super().__init__()
        self._status = 'Dead'

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def modify(self, *args, **kwargs):
        pass

    def notify(self):
        pass
