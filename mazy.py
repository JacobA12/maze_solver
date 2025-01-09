from cell import Cell

class Maze:
  def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
    self.x1 = x1
    self.y1 = y1
    self.num_rows = num_rows
    self.num_cols = num_cols
    self.cell_size_x = cell_size_x
    self.cell_size_y = cell_size_y
    self.win = win
    self._create_cells()
    
  def _create_cells(self):
    self._cells = []
    for col in range(self.num_cols):
      column = []
      for row in range(self.num_rows):
        cell = Cell(
          self.x1 + col * self.cell_size_x,
          self.y1 + row * self.cell_size_y,
          self.cell_size_x,
          self.cell_size_y,
          self.win
        )
        cell._draw_cell()
        column.append(cell)
      self._cells.append(column)
  
  def _draw_cell(self,i,j):
    