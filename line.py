from point import Point


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas, fill):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill, width=2)
