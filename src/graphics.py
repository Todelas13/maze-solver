from tkinter import Tk, BOTH, Canvas

class Window():

    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.canvas = Canvas(self.__root,bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True
        while(self.running):
            self.redraw()

    def close(self):
        self.running = False
    
    def draw_line(self,line,fill_color):
        line.draw(self.canvas,fill_color)

class Point():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():

    def __init__(self, a, b):
        self.pointa = a
        self.pointb = b
    
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.pointa.x, self.pointa.y, self.pointb.x, self.pointb.y, fill=fill_color, width=3
        )







