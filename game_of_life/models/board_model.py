from .abstract_model import AbstractModel
from .cell_model import CellModel
from random import randint
import threading as th


class BoardModel(AbstractModel):
    def __init__(self, rows, columns, period):
        super().__init__()
        self._rows = rows
        self._columns = columns
        self._grid = [[CellModel() for column in range(self._columns)] for row in range(self._rows)]
        self._period = period
        self._cycle = th.Timer(self._period, self._update_cell_status)
        self._generate_board()
        self._running = False

    @property
    def cycle(self):
        return self._cycle

    def _generate_board(self):
        for row in self._grid:
            for column in row:
                # there is a 33% chance the cells spawn alive.
                chance_number = randint(0, 9)
                if chance_number == 1:
                    column.status = 'Alive'

    def _check_neighbour(self, check_row, check_column):
        # how deep the search is:
        search_min = -1
        search_max = 2

        # empty list to append neighbours into.
        neighbour_list = []
        for row in range(search_min, search_max):
            for column in range(search_min, search_max):
                neighbour_row = check_row + row
                neighbour_column = check_column + column

                valid_neighbour = True

                if (neighbour_row == check_row) and (neighbour_column == check_column):
                    valid_neighbour = False

                if (neighbour_row < 0) or (neighbour_row >= self._rows):
                    valid_neighbour = False

                if (neighbour_column < 0) or (neighbour_column >= self._columns):
                    valid_neighbour = False

                if valid_neighbour:
                    neighbour_list.append(self._grid[neighbour_row][neighbour_column])
        return neighbour_list

    def _update_cell_status(self):
        # cells list for living cells to kill and cells to resurrect or keep alive
        goes_alive = []
        gets_killed = []

        for row in range(len(self._grid)):
            for column in range(len(self._grid[row])):

                # check neighbour pr. square:
                check_neighbour = self._check_neighbour(row, column)

                living_neighbours_count = []

                for neighbour_cell in check_neighbour:
                    # check live status for neighbour_cell:
                    if neighbour_cell.status == 'Alive':
                        living_neighbours_count.append(neighbour_cell)

                cell_object = self._grid[row][column]
                status_main_cell = cell_object.status

                # If the cell is alive, check the neighbour status.
                if status_main_cell == 'Alive':
                    if len(living_neighbours_count) < 2 or len(living_neighbours_count) > 3:
                        gets_killed.append(cell_object)

                    if len(living_neighbours_count) == 3 or len(living_neighbours_count) == 2:
                        goes_alive.append(cell_object)

                else:
                    if len(living_neighbours_count) == 3:
                        goes_alive.append(cell_object)

        # sett cell statuses
        for cell_items in goes_alive:
            cell_items.status = 'Alive'

        for cell_items in gets_killed:
            cell_items.status = 'Dead'
        self._cycle = th.Timer(self._period, self._update_cell_status)
        self._cycle.start()
        self.notify()

    def modify(self, *args, **kwargs):
        self._running = not self._running
        if self._running:
            self._cycle = th.Timer(self._period, self._update_cell_status)
            self._cycle.start()
        else:
            self._cycle.cancel()

    def notify(self):
        for obs in self._obs_list.values():
            obs.update(self._grid)
