# goal
- build maze builder / solver using python and tkinter

# structure

## main
- main
    - runs program

## render components
- window class
    - generate a window that displays the maze
    - methods
        - redraw
        - wait for close
        - close
        - draw_line(Line, fill_color)
## 2D components
- point class
    - data class representing a point on the canvas
    - attrs
        - x
        - y
- line class
    - data class representing a line between two points
    - attrs
        - points (list)
    - methods
        - draw(canvas, color): this should call canvas.create_line()
## maze components
- cell class
    - a collection of data that represents a box, its walls and where it lives on an x/y grid
    - attrs
        - has_left_wall
        - has_right_wall
        - has_top_wall
        - has_bottom_wall
        - _x1
        - _x2
        - _y1
        - _y2
        - _win
        - visited = false
    - methods
        - draw(top left, bottom right): depending on if it has certain walls, draw them
        - draw_move(to cell, undo): lines should be drawn from center of a box to center of the other box. if undo flag is not set, make line red, otherwise grey
- maze class
    - holds all the cell classes in a 2d grid of lists
    - attrs
        - x1
        - y1
        - num_rows
        - num_cols
        - cell_size_x
        - cell_size_y
        - win
        - seed (optional)
    - methods
        - create cells
        - draw cells
        - animate
        - break entrance exit
        - break walls
        - reset visited cells
        - solve: this is a function called by users (the inn keeper)
        - _solve_r(): this is a helper function that does the real math (the chef)