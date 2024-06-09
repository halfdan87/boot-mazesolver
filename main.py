from maze import Maze
from point import Point
from line import Line
from window import Window
from cell import Cell


def main():
    win = Window(800, 600)

    m1 = Maze(Point(50, 50), 10, 50, Point(10, 10), win)

    m1.solve()

    win.wait_for_close()


main()
