from grid_elements import Line, Point
import time
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size, win, seed = None):
        # top left corner
        self.x1 = x1
        self.y1 = y1
        
        # maze size
        self.num_rows = num_rows
        self.num_cols = num_cols
        
        # size of a cell in pixels
        self.cell_size = cell_size
        self.cells = []

        # window / canvas from tkinter
        self.win = win
        self.canvas = win.canvas

        if seed != None:
            random.seed(seed)

        self.generate_maze()

    def generate_maze(self):
        self.create_cells()
        self.draw_cells()
        self.break_entrance_and_exit()


    def create_cells(self):
        # creates cells in rows and columns

        columns_list = []
        
        for x in range (self.num_cols):
            width = x * self.cell_size

            rows_list = []    
            for y in range(self.num_rows):
                height = y * self.cell_size
                
                # creates a cell object at a specific location based on the size of the cells

                new_cell = Cell(Point(self.x1 + width, self.y1 + height))
                if x == 0:
                    #print("turn off left")
                    new_cell.valid_directions["west"] = 0
                if x == self.num_cols-1:
                    #print("turn off right")
                    new_cell.valid_directions["east"] = 0
                if y == 0:
                    #print("turn off up")
                    new_cell.valid_directions["north"] = 0
                if y == self.num_rows-1:
                    #print("turn off down")
                    new_cell.valid_directions["south"] = 0

                rows_list.append(new_cell)
                print(f"x:{x},y:{y} - n:{new_cell.valid_directions["north"]},e:{new_cell.valid_directions["east"]},s:{new_cell.valid_directions["south"]},W:{new_cell.valid_directions["west"]}")
            
            columns_list.append(rows_list)
            
        self.cells = columns_list
        return
        
        '''
        turn it sideways and it makes more sense :')
        it builds one column at a time atm
        cells = [column1[row1,row2,row3],
                column2[row1,row2,row3],
                column3[row1,row2,row3]]
        '''

        
    def draw_cells(self):

        for cells_list in self.cells:
            for cell in cells_list:
                cell.draw(self.canvas,'green')
                self.animate()
                #print(cell)
    
    def break_entrance_and_exit(self):
        
        # really hard to parse which cell is which, same with direction
        self.cells[0][0].lines[3].active = False
        self.cells[self.num_cols-1][self.num_rows-1].lines[1].active = False
        self.draw_cells()
        
    def animate(self):
        self.win.redraw()
        time.sleep(.05)
        
    def break_walls_r(self):

        self.cells[0][0].visited = True
        while True:
            unvisited = []
            for cell in self.cells:
                #0001
                #hmmm maybe binary broken walls list? vs valid directions maybe we OR it against valids?
                for direction in cell.valid_directions:
                    if direction == 1:
                        pass
                pass
            # hmmm how to check all the valid locations
            # if on the border, dont check border directions for other cells
            
            pass
        '''
        50% change row column, if the column is on the bounds DONT GO THAT WAY

        mark cell visted
        loop
        - create a list to hold the xy values that you need to visit
        - check cells that are adacent to current cell, keep track of any that hae NOT been visted
        - if there are zero directions to go, draw the current cell and return
        - else, pick a random direction
        - knock down the walls between the current cell and chosen cell
        move to the chosen cell by calling break walls
        '''
        pass

class Cell():
    def __init__(self, point, width = 50):

        self.visted = False
        self.width = width

        self.canvas = ''
        self.fill_color = ''

        # main point, the origin location
        self.point = point

        # defines list of 4 points that make up the cell
        self.points = [self.point, 
                       Point(point.x + self.width, point.y), 
                       Point(point.x + self.width, point.y + self.width),
                       Point(point.x, point.y + self.width)]
        
        # connects the points together into lines
        self.lines = [Line(self.points[0], self.points[1]),
                 Line(self.points[1], self.points[2]),
                 Line(self.points[2], self.points[3]),
                 Line(self.points[3], self.points[0])]

        self.center = Point(point.x + (self.width / 2),
                            point.y + (self.width / 2))

        self.valid_directions = {"north":1,"east":1,"south":1,"west":1}

    def break_wall(self):
        # give cell / direction, set to false and redraw cells

        pass
    
    def draw(self, canvas, fill_color):
        # draws the cell, if a area is missing a wall, draw that line segment white
        color = fill_color

        for line in self.lines:
            if line.active == True:
                color = fill_color
            else:
                color = 'white'
            line.draw(canvas,color)
        
    def draw_move(self, to_cell, canvas, undo = False):
        center_line = Line(self.center,to_cell.center)
        if undo == False:
            fill_color = 'red'
        else:
            fill_color = 'gray'
        center_line.draw(canvas, fill_color)
        pass

