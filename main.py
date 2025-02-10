from window import Window
from grid_elements import Point, Line
from maze import Cell, Maze

def test_lines(win):
    point_a = Point(50,100)
    point_b = Point(0,600)
    point_c = Point(0,600)
    point_d = Point(400,0)

    line_a = Line(point_a,point_b)
    line_a.draw(win.canvas, "black")

    line_b = Line(point_c,point_d)
    line_b.draw(win.canvas, "red")

def test_cells(win):
    cell_a = Cell(Point(60,60))
    cell_a.has_left_wall = False
    cell_a.draw(win.canvas, "green")
    
    cell_b = Cell(Point(160,300))
    cell_b.has_left_wall = False
    cell_b.draw(win.canvas, "green")
    cell_b.draw_move(cell_a, win.canvas, True)

def test_maze(win):
    maze_a = Maze(200,100,5,5,50,win)

def main():
    win = Window(800,600)
    
    # render
    # test_lines(win)
    # test_cells(win)
    test_maze(win)
    win.wait_for_close()

if __name__ == "__main__":
    main()