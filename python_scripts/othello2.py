# <Rachel Davel davel013>
# I understand this is a graded, individual examination that may not be
# discussed with anyone.  I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing
# any aspect of the examination with anyone will result in failing the course.
# I further certify that this program represents my own work and that none of
# it was obtained from any source other than material presented as part of the
# course.

import turtle
import random
import math

def makeSquare(size):
    i = 0
    turtle.color('black')
    turtle.fillcolor('green')
    turtle.begin_fill()
    i= 0
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
        i += 1
    turtle.end_fill()
    turtle.penup()
    turtle.forward(size)
    turtle.pendown()

def chain_squares(size):
    i = 0
    for i in range(4):
        makeSquare(size)
        makeSquare(size)
        i+= 1

def drawBoard(size):
    turtle.hideturtle()
    i=0
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-(size*4),(size*4))
    turtle.pendown()
    for i in range(8):
        chain_squares(size)
        turtle.back(size*8)
        turtle.right(90)
        turtle.forward(size)
        turtle.left(90)
        i += 1

def board_set(size):
    turtle.penup()
    turtle.left(90)
    turtle.forward(size*5.5)
    turtle.right(90)
    turtle.forward(size*3.5)
    turtle.color('white')
    turtle.shape('circle')
    turtle.stamp()
    turtle.forward(size)
    turtle.color('black')
    turtle.stamp()
    turtle.right(90)
    turtle.forward(size)
    turtle.color('white')
    turtle.stamp()
    turtle.right(90)
    turtle.forward(size)
    turtle.color('black')
    turtle.stamp()

def write_headers(size):
    turtle.hideturtle()
    i = 0
    turtle.color("black")
    turtle.penup()
    turtle.goto(-225,260)
    turtle.right(180)
    while i < 8:
        turtle.forward(50)
        turtle.pendown()
        turtle.write(i)
        turtle.penup()
        i += 1

def write_sides(size):
    i= 0
    turtle.goto(-220,270)
    turtle.right(90)
    while i < 8:
        turtle.forward(50)
        turtle.write(i)
        i += 1

def complete_board():
    size= 50
    drawBoard(size)
    board_set(size)
    write_headers(size)
    write_sides(size)

def board_coordinates():
    board=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,2,0,0,0],[0,0,0,2,1,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    coordinates= [[(-175,225),(-125,225),(-75,225),(-25,225),(25,225),(75,225),(125,225),(175,225)],[(-175,175),(-125,175),(-75,175),(-25,175),(25,175),(75,175),(125,175),(175,175)],[(-175,125),(-125,125),(-75,125),(-25,125),(25,125),(75,125),(125,125),(175,125)],[(-175,75),(-125,75),(-75,75),(-25,75),(25,75),(75,75),(125,75),(175,75)],[(-175,25),(-125,25),(-75,25),(-25,25),(25,25),(75,25),(125,25),(175,25)],[(-175,-25),(-125,-25),(-75,-25),(-25,-25),(25,-25),(75,-25),(125,-25),(175,-25)],[(-175,-75),(-125,-75),(-75,-75),(-25,-75),(25,-75),(75,-75),(125,-75),(175,-75)],[(-175,-125),(-125,-125),(-75,-125),(-25,-125),(25,-125),(75,-125),(125,-125),(175,-125)]]
    return board,coordinates

def player_move():
    player_move = turtle.textinput("Player Move","Where would you like to place a piece?(pleas use commas to separate the row and column) ")
    col= int(player_move[0])
    row= int(player_move[2])
    return col, row

def closing_message():
    if player_score > computer_score:
        turtle.text("Congrats! You're the winner!")
    else:
        turtle.text("Bummer!  You lost!")
    print player_score
    print computer_score

def selectNextPlay():
    #pure function
    #called to get computer's next play
    #make a random choice from valid options
def isValidMove(board,row,col,color):
    if board[row][col] !=:
        return False

    #will return True if the specified move is "valid"
    # to be valid, the space must be unoccupied
    #sy least one neighbor must have an opponent tile
    # at least one straight line must end with the correct color

def getValidMoves(board,color):
    #scan every cell and return a list of row,column tuples that are valid plays
    # for the indicated color

def find_neighbors(row,col,board):
    neighbors=[]
    if col == 0 and row == 0:
        neighbors.append((col+1,row))
        neighbors.append((col,row+1))
        neighbors.append((col+1,row+1))
    if col==7 and row==7:
        neighbors.append((col-1,row))
        neighbors.append((col,row+1))
        neighbors.append((col-1,row+1))
    if col== 0 and row != 0 or 7:
        neighbors.append((col,row-1))
        neighbors.append((col,row+1))
        neighbors.append((col+1,row))
        neighbors.append((col+1,row-1))
        neighbors.append((col+1,row+1))
    if col==7 and row != 0 or 7:
        neighbors.append((col-1,row))
        neighbors.append((col,row-1))
        neighbors.append((col,row+1))
        neighbors.append((col-1,row+1))
        neighbors.append((col-1,row-1))
    else:
        neighbors.append((col+1,row))
        neighbors.append((col-1,row))
        neighbors.append((col,row+1))
        neighbors.append((col,row-1))
        neighbors.append((col+1,row+1))
        neighbors.append((col-1,row-1))
        neighbors.append((col+1,row-1))
        neighbors.append((col-1,row+1))
    return neighbors

def main():
    print(complete_board())
    board,coordinates= board_coordinates()
    col,row=player_move()


if __name__ == '__main__':
    main()
