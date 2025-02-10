from tkinter import Tk, BOTH, Canvas

# global class
class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.root = Tk()
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.title("Maze Solver")
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(width=self.width,height=self.height) 
        self.canvas.pack(expand=1)

        self.running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        # calls the draw function from the line class
        line.draw(self.canvas, fill_color)
