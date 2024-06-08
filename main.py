from point import Point
from line import Line
from window import Window
from cell import Cell


def main():
    win = Window(800, 600)

    line = Line(Point(0, 0), Point(100, 100))
    win.draw_line(line, "red")

    cell = Cell(Point(20, 23), Point(50, 120), win)
    cell.leftWall = False
    cell.draw()

    cell2 = Cell(Point(50, 53), Point(120, 230), win)
    cell2.upWall = False
    cell2.draw()

    cell.draw_move(cell2)

    win.wait_for_close()


main()
