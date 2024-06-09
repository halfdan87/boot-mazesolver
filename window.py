from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze solver")
        self.root.geometry(f"{width}x{height}")
        self.running = False
        self.canvas = Canvas(self.root)
        self.canvas.pack(fill=BOTH, expand=True)
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True

        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill):
        line.draw(self.canvas, fill)
