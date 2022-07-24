from game_of_life.controllers.controller import Controller
from game_of_life.controllers.app import App
from argparse import ArgumentParser

# Number of cells in row and column
ROWS = 30
COLUMNS = 30
# Size of window in pixels
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
# Time for updating cell status
PERIOD = 1


def main():
    parser = ArgumentParser(description='Game of life')
    parser.add_argument('--rows', dest='rows', type=int, help="Number of cells in column")
    parser.add_argument('--columns', dest='columns', type=int, help="Number of cells in row")
    parser.add_argument('--window_width', dest='window_width', type=int, help="Width of window in pixels")
    parser.add_argument('--window_height', dest='window_height', type=int, help="Height of window in pixels")
    parser.add_argument('--period', dest='period', type=float, help="Time for updating cell status")
    args = parser.parse_args()
    global ROWS, COLUMNS, WINDOW_WIDTH, WINDOW_HEIGHT, PERIOD

    if args.rows:
        ROWS = args.rows
    if args.columns:
        COLUMNS = args.columns
    if args.window_width:
        WINDOW_WIDTH = args.window_width
    if args.window_height:
        WINDOW_HEIGHT = args.window_height
    if args.period:
        PERIOD = args.period

    controller = Controller()
    app = App(controller, WINDOW_HEIGHT, WINDOW_WIDTH, ROWS, COLUMNS, PERIOD)
    app.run_app()


if __name__ == '__main__':
    main()
