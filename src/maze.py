import random
from cell import *
from graphics import *
import time

class Maze():

    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win,seed=None) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        if seed is not None :
            random.seed(seed)
        self._create_cells() 

    def _create_cells(self):
        #nao foi implementado com o o offset para um x1,y1 específico
        for i in range(self.num_rows):
            new_row = []
            for j in range(self.num_cols):
                # px_incial = (j*self.x1) + self.x1
                # py_inicial = (i*self.y1) + self.y1
                # ponto_a = Point(px_incial,py_inicial)
                # ponto_b = Point(px_incial+self.cell_size_x,py_inicial+self.cell_size_y)
                cell_to_add = Cell(Point((j*self.cell_size_x),(i*self.cell_size_y)),Point((j*self.cell_size_x)+self.cell_size_x,(i*self.cell_size_y)+self.cell_size_y),self.win)
                new_row.append(cell_to_add)
            self._cells.append(new_row)
        
        print(len(self._cells))
        self._draw_cell()

    def _draw_cell(self):

        for row in self._cells:
            for col in row:
                colx1 = col._x1
                colx2 = col._x2
                coly1 = col._y1
                coly2 = col._y2
                print(colx1,coly1)
                print(colx2,coly2)
                col.draw()
                self._animate()
        self._break_entrance_and_exit()
        self._cells[0][0].draw()
        self._cells[self.num_rows-1][self.num_cols-1].draw()
        self._animate()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.02)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall=False
        self._cells[self.num_rows-1][self.num_cols-1].has_bottom_wall=False
    
    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True
        while(True):
            possible_directions = []
            north = [i-1,j,"north"]
            south = [i+1,j,"south"]
            west = [i,j-1,"west"]
            east = [i,j+1,"east"]

            if i > 0 and not self._cells[i-1][j].visited:
                possible_directions.append(north)
            if i < (self.num_rows -1) and not self._cells[i+1][j].visited:
                possible_directions.append(south)
            if j > 0 and not self._cells[i][j-1].visited:
                possible_directions.append(west)
            if j< (self.num_cols - 1) and not self._cells[i][j+1].visited:
                possible_directions.append(east)
            
            if not possible_directions:
                break
            
            direction = random.choice(possible_directions)
            if direction[2] == "north":
                self._cells[i][j].has_top_wall = False
                self._cells[direction[0]][direction[1]].has_bottom_wall = False
                self._cells[i][j].draw()
                self._cells[direction[0]][direction[1]].draw()
                self._animate()
            elif direction[2] == "south":
                self._cells[i][j].has_bottom_wall = False
                self._cells[direction[0]][direction[1]].has_top_wall = False
                self._cells[i][j].draw()
                self._cells[direction[0]][direction[1]].draw()
                self._animate()
            elif direction[2] == "east":
                self._cells[i][j].has_right_wall = False
                self._cells[direction[0]][direction[1]].has_left_wall = False
                self._cells[i][j].draw()
                self._cells[direction[0]][direction[1]].draw()
                self._animate()
            elif direction[2] == "west":
                self._cells[i][j].has_left_wall = False
                self._cells[direction[0]][direction[1]].has_right_wall = False
                self._cells[i][j].draw()
                self._cells[direction[0]][direction[1]].draw()
                self._animate()

            self._break_walls_r(direction[0],direction[1])
    
    def _reset_cells_visited(self):
        for row in self._cells:
            for col in row:
                col.visited = False
    
    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == (self.num_rows-1) and (j == self.num_cols -1):
            return True
        
        if i > 0 and not self._cells[i-1][j].visited and not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            check = self._solve_r(i-1,j)
            if check:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j],True)
        if i < (self.num_rows -1) and not self._cells[i+1][j].visited and not self._cells[i][j].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            check = self._solve_r(i+1,j)
            if check:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j],True)
        if j > 0 and not self._cells[i][j-1].visited and not self._cells[i][j].has_left_wall:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            check = self._solve_r(i,j-1)
            if check:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1],True)
        if j< (self.num_cols - 1) and not self._cells[i][j+1].visited and not self._cells[i][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            check = self._solve_r(i,j+1)
            if check:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1],True)

        return False
    


    
    





            



