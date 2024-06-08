from point import Point
from window import Window
from line import Line


class Cell:
    def __init__(self, topLeftPoint, bottomRightPoint, window):
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
        if self.leftWall:
            self.window.draw_line(Line(self.topLeftPoint, self.bottomLeftPoint), "blue")
        if self.rightWall:
            self.window.draw_line(Line(self.topRightPoint, self.bottomRightPoint), "blue")
        if self.upWall:
            self.window.draw_line(Line(self.topRightPoint, self.topLeftPoint), "blue")
        if self.downWall:
            self.window.draw_line(Line(self.bottomLeftPoint, self.bottomRightPoint), "blue")

    def draw_move(self, to_cell, undo=False):
        colour = "red"
        if undo:
            colour = "gray"
        self.window.draw_line(Line(self.center, to_cell.center), colour)
