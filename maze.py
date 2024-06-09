from re import search
from cell import Cell
from point import Point
import time
import random


class Maze:
    def __init__(self, pos_point, rows, cols, cell_size, window=None):
        random.seed(0)

        self.cells = []
        self.pos_point = pos_point
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.window = window
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        self.cells = [
            [
                Cell(
                    Point(
                        self.pos_point.x + (i - 0.5) * self.cell_size.x,
                        self.pos_point.y + (j - 0.5) * self.cell_size.y,
                    ),
                    Point(
                        self.pos_point.x + (i + 0.5) * self.cell_size.x,
                        self.pos_point.y + (j + 0.5) * self.cell_size.y,
                    ),
                    self.window,
                )
                for j in range(self.rows)
            ]
            for i in range(self.cols)
        ]
        for i in range(self.cols):
            for j in range(self.rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        self.cells[i][j].draw()

    def _break_entrance_and_exit(self):
        entrance_cell = self.cells[0][0]
        entrance_cell.upWall = False
        self._draw_cell(0, 0)

        exit_cell = self.cells[self.cols - 1][self.rows - 1]
        exit_cell.downWall = False
        self._draw_cell(self.cols - 1, self.rows - 1)

    def _break_walls_r(self, i, j):
        self.cells[i][j].visited = True

        while True:
            to_visit = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self.cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            # right
            if i < self.cols - 1 and not self.cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            # up
            if j > 0 and not self.cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            # down
            if j < self.rows - 1 and not self.cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            direction = random.randrange(len(to_visit))
            next = to_visit[direction]

            if next[0] == i + 1:
                self.cells[i][j].rightWall = False
                self.cells[i + 1][j].leftWall = False
            # left
            if next[0] == i - 1:
                self.cells[i][j].leftWall = False
                self.cells[i - 1][j].rightWall = False
            # down
            if next[1] == j + 1:
                self.cells[i][j].downWall = False
                self.cells[i][j + 1].upWall = False
            # up
            if next[1] == j - 1:
                self.cells[i][j].upWall = False
                self.cells[i][j - 1].downWall = False

            self._break_walls_r(next[0], next[1])

    def _reset_cells_visited(self):
        for i in range(self.cols):
            for j in range(self.rows):
                self.cells[i][j].visited = False

    def _animate(self):
        if self.window is None:
            return
        self.window.redraw()
        time.sleep(0.05)

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, x, y):
        self._animate()
        cur = self.cells[x][y]
        cur.visited = True
        if x == self.cols - 1 and y == self.rows - 1:
            return True

        dirs = [Point(-1, 0), Point(1, 0), Point(0, -1), Point(0, 1)]
        walls = [cur.leftWall, cur.rightWall, cur.upWall, cur.downWall]

        for i in range(4):
            self._animate()
            new_x, new_y = dirs[i].x + x, dirs[i].y + y
            if not walls[i] and 0 <= new_x < self.cols and 0 <= new_y < self.rows:
                target = self.cells[new_x][new_y]
                if not target.visited:
                    if self._solve_r(new_x, new_y):
                        return True
                    cur.draw_move(target, undo=True)
        return False
