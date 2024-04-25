from graphics import *
from cell import *
from maze import *
def main():
    win = Window(800,600)
    #seed = 10
    # diag = Line(Point(0,0),Point(800,600))
    # win.draw_line(diag,"black")
    # for i in range(0,800,100):
    #     for j in range(0,600,100):
    #         new_square = Cell(Point(j,i),Point(j+100,i+100),win)
    #         squares.append(new_square)
    # for sqr in squares:
    #     sqr.draw()
    # squares[0].draw_move(squares[1])
    maze = Maze(0,0,12,16,50,50,win)
    maze.solve()
    win.wait_for_close()

main()