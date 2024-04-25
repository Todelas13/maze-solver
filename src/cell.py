from graphics import *
class Cell():

    def __init__(self,a:Point,b:Point,win:Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = a.x
        self._x2 = b.x
        self._y1 = a.y
        self._y2 = b.y
        self._win = win
        self.visited = False

    def draw(self):
        if self.has_left_wall:
            line_left = Line(Point(self._x1,self._y1),Point(self._x1,self._y2))
            self._win.draw_line(line_left,"black")
        else:
            line_left = Line(Point(self._x1,self._y1),Point(self._x1,self._y2))
            self._win.draw_line(line_left,"white")
        if self.has_right_wall:
            line_right = Line(Point(self._x2,self._y1),Point(self._x2,self._y2))
            self._win.draw_line(line_right,"black")
        else:
            line_right = Line(Point(self._x2,self._y1),Point(self._x2,self._y2))
            self._win.draw_line(line_right,"white")
        if self.has_top_wall:
            line_top = Line(Point(self._x1,self._y1),Point(self._x2,self._y1))
            self._win.draw_line(line_top,"black")
        else:
            line_top = Line(Point(self._x1,self._y1),Point(self._x2,self._y1))
            self._win.draw_line(line_top,"white")
        if self.has_bottom_wall:
            line_bottom = Line(Point(self._x1,self._y2),Point(self._x2,self._y2))
            self._win.draw_line(line_bottom,"black")
        else:
            line_bottom = Line(Point(self._x1,self._y2),Point(self._x2,self._y2))
            self._win.draw_line(line_bottom,"white")
    
    def draw_move(self, to_cell:'Cell', undo=False):
        center_x = (self._x1 + self._x2) /2
        center_y = (self._y1 + self._y2) / 2
        print(center_x,center_y)
        cell_x = (to_cell._x2 + to_cell._x1) /2
        cell_y = (to_cell._y1 + to_cell._y2) /2
        print(cell_x,cell_y)
        linha = Line(Point(center_x,center_y),Point(cell_x,cell_y))
        if undo:    
            self._win.draw_line(linha,"red")
        else:
            self._win.draw_line(linha,"green")



        
