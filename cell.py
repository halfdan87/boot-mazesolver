from point import Point
from window import Window
from line import Line


class Cell:
    def __init__(self, topLeftPoint, bottomRightPoint, window=None):
        self.visited = False
        self.leftWall = True
        self.rightWall = True
        self.upWall = True
        self.downWall = True
        self.window = window
        self.topLeftPoint = topLeftPoint
        self.bottomRightPoint = bottomRightPoint
        self.bottomLeftPoint = Point(topLeftPoint.x, bottomRightPoint.y)
        self.topRightPoint = Point(bottomRightPoint.x, topLeftPoint.y)
        self.center = Point(
            (self.topRightPoint.x + self.topLeftPoint.x) / 2,
            (self.topLeftPoint.y + self.bottomLeftPoint.y) / 2,
        )

    def draw(self):
        if self.window is None:
            return
        if self.leftWall:
            self.window.draw_line(Line(self.bottomLeftPoint, self.topLeftPoint), "blue")
        else:
            self.window.draw_line(Line(self.bottomLeftPoint, self.topLeftPoint), "white")

        if self.rightWall:
            self.window.draw_line(Line(self.bottomRightPoint, self.topRightPoint), "blue")
        else:
            self.window.draw_line(Line(self.bottomRightPoint, self.topRightPoint), "white")

        if self.upWall:
            self.window.draw_line(Line(self.topLeftPoint, self.topRightPoint), "blue")
        else:
            self.window.draw_line(Line(self.topLeftPoint, self.topRightPoint), "white")

        if self.downWall:
            self.window.draw_line(Line(self.bottomLeftPoint, self.bottomRightPoint), "blue")
        else:
            self.window.draw_line(Line(self.bottomLeftPoint, self.bottomRightPoint), "white")

    def draw_move(self, to_cell, undo=False):
        if self.window is None:
            return
        colour = "red"
        if undo:
            colour = "gray"
        self.window.draw_line(Line(self.center, to_cell.center), colour)
