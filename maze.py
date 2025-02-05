from grid_elements import Line, Point
import time

class Cell():
    def __init__(self, point, width = 50):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
        self.width = width

        self.canvas = ''
        self.fill_color = ''

        self.points = [point, 
                       Point(point.x + self.width, point.y), 
                       Point(point.x + self.width, point.y + self.width),
                       Point(point.x, point.y + self.width)]

        self.center = Point(point.x + (self.width / 2),
                            point.y + (self.width / 2))
        #self.x = point.x
        #self.y = point.y
        
        # self.y1
        # self.y2
        # self.win
    def draw(self, canvas, fill_color):
        lines = [Line(self.points[0], self.points[1]),
                 Line(self.points[1], self.points[2]),
                 Line(self.points[2], self.points[3]),
                 Line(self.points[3], self.points[0])]
        color = fill_color
        if self.has_top_wall == False:
            color = 'white'
        else:
            color = fill_color
        lines[0].draw(canvas, color)
            #lines.append(Line(self.points[0], self.points[1]))
        if self.has_right_wall == False:
            color = 'white'
        else:
            color = fill_color
        lines[1].draw(canvas, color)
            #lines.append(Line(self.points[1], self.points[2]))
        if self.has_bottom_wall == False:
            color = 'white'
        else:
            color = fill_color
        lines[2].draw(canvas, color)
            #lines.append(Line(self.points[2], self.points[3]))
        if self.has_left_wall == False:
            color = 'white'
        else:
            color = fill_color
        lines[3].draw(canvas, color)
            #lines.append(Line(self.points[3], self.points[0]))
        #for line in lines:
            #line.draw(canvas, fill_color)
        
    def draw_move(self, to_cell, canvas, undo = False):
        center_line = Line(self.center,to_cell.center)
        if undo == False:
            fill_color = 'red'
        else:
            fill_color = 'gray'
        center_line.draw(canvas, fill_color)
        pass

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size = cell_size
        self.win = win
        self.canvas = win.canvas

        self.create_cells()
        self.break_entrance_and_exit()

    def create_cells(self):
        self.cells = []
        columns_list = []

        for x in range (self.num_cols):
            rows_list = []    
            for y in range(self.num_rows):
                #print(y)
                rows_list.append(Cell(Point(self.x1 + (x * self.cell_size), self.y1 + (y * self.cell_size))))
            #print(x)
            columns_list.append(rows_list)
            
        self.cells = columns_list
        self.draw_cells()

        return
    def draw_cells(self):
        for cells_list in self.cells:
            for cell in cells_list:
                cell.draw(self.canvas,'green')
                self.animate()
                #print(cell)
    
    def break_entrance_and_exit(self):
        self.cells[0][0].has_left_wall = False
        self.cells[self.num_cols-1][self.num_rows-1].has_right_wall = False

        
    def animate(self):
        self.win.redraw()
        time.sleep(.05)
        