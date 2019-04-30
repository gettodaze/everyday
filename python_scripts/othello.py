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
    turtle.speed(1000)
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

#this function creates the list that we will be using for the board values
def board_coordinates(): #call like board[1][2]
    board=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,2,0,0,0],[0,0,0,2,1,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    coordinates= [[(-175,225),(-125,225),(-75,225),(-25,225),(25,225),(75,225),(125,225),(175,225)],[(-175,175),(-125,175),(-75,175),(-25,175),(25,175),(75,175),(125,175),(175,175)],[(-175,125),(-125,125),(-75,125),(-25,125),(25,125),(75,125),(125,125),(175,125)],[(-175,75),(-125,75),(-75,75),(-25,75),(25,75),(75,75),(125,75),(175,75)],[(-175,25),(-125,25),(-75,25),(-25,25),(25,25),(75,25),(125,25),(175,25)],[(-175,-25),(-125,-25),(-75,-25),(-25,-25),(25,-25),(75,-25),(125,-25),(175,-25)],[(-175,-75),(-125,-75),(-75,-75),(-25,-75),(25,-75),(75,-75),(125,-75),(175,-75)],[(-175,-125),(-125,-125),(-75,-125),(-25,-125),(25,-125),(75,-125),(125,-125),(175,-125)]]
    # we could fill the list with all 0s or something, these aren't necessary
    return board,coordinates
#this function is letter the player input their move
def computer_play(board):
    playHere= random.randint(board)
    col= playHere[0]
    row= playHere[1]
    return row,col

def selectNextPlay():
    player_move = turtle.textinput("Player Move","Where would you like to place a piece?(pleas use commas to separate the row and column) ")
    col= int(player_move[0])
    row= int(player_move[2])
    return col, row

#find surrounding pieces that could potentially be played in
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

#narrows down list of surrounding pieces to actually valid spaces
def getValidMoves(board,color,neighbors):
    i = 0
    validMoves= []
    if color == 'black':
        while i < len(neighbors):
            position= neighbors[i]
            if board[position[0]][position[1]] == 1:
                validMoves.append(neighbors[i])
            i += 1
        return validMoves
    if color == 'white':
        while i < len(neighbors):
            position= neighbors[i]
            if board[position[0]][position[1]] == 2:
                validMoves.append(neighbors[i])
            i+=  1
        return validMoves

#determines if the play connects pieces and is valid
def changeTrain(validMoves,board,color,row,col,neighbors):
    flipList= [(row,col),(1,1),(2,2)]
    return flipList



'''    place_row - row
    for row, col in validMoves:
        token = board[row][col]
        change = 0
        while token == 2:
            row -= 1  (or col -=)
        neighbors= neighbors(thing)
        flipList.append(neighbors)
    return flipList'''


# call neighbors again and then

def isValidMove(board,row,col,color,flipList):
    if len(flipList) < 1:
        return False
    else:
        return True

def place_move(color,row,col,coordinates,flipList):
    i = 0
    turtle.penup()
    turtle.color(color)
    turtle.shape("circle")
    location= coordinates[row][col]
    turtle.goto(location)
    turtle.showturtle()
    turtle.pendown()
    turtle.stamp()
    while i < len(flipList):
        spot= flipList[i]
        k= spot[0]
        y= spot[1]
        place= coordinates[k][y]
        turtle.penup()
        turtle.color(color)
        turtle.shape("circle")
        turtle.goto(place)
        turtle.showturtle()
        turtle.pendown()
        turtle.stamp()
        i += 1

#keeps track of player and computer points
def scoreCard(flipList,playerScore,computerScore,color):
    i = 0
    if color == 'black':
        playerScore += 1
        while i <len(flipList):
            playerScore += 1
            computerScore -= 1
            i += 1
    if color == 'white':
        computerScore += 1
        while i <len(flipList):
            computerScore += 1
            playerScore -= 1
            i += 1
    return playerScore,computerScore

def board_update(flipList,color,board):
    i = 0
    if color == 'white':
        while i < len(flipList):
            spot= []
            spot += flipList[i] # in theory (5,6)
            m= spot[0]
            n= spot[1]
            board[m][n] = 1
            i+= 1
    if color == 'black':
        while i < len(flipList):
            spot= []
            spot += flipList[i] # in theory (5,6)
            m= spot[0]
            n= spot[1]
            board[m][n] = 2
            i += 1
    return board

def main():
    size= 50 #this is the size of the squares
    playerScore= 0
    computerScore= 0
    print(drawBoard(size))
    print(board_set(size))
    print(write_headers(size))
    print(write_sides(size))
    board,coordinates= board_coordinates()
    while playerScore != 32 and computerScore != 32:
        color= "black"
        col,row = selectNextPlay()
        neighbors=find_neighbors(row,col,board)
        print(neighbors)
        validMoves= getValidMoves(board,color,neighbors)
        print(validMoves)
        flipList=changeTrain(board,validMoves,color,row,col,neighbors)
        print(flipList)
        place_move(color,row,col,coordinates,flipList)
        playerScore,computerScore= scoreCard(flipList,playerScore,computerScore,color)
        print(playerScore)
        isValidMove(board,row,col,color,flipList)
        board= board_update(flipList,color,board)
        color= 'white'
        col,row= computer_play(board)
        neighbors=find_neighbors(row,col,board)
        validMoves= getValidMoves(board,color,neighbors)
        #while len(validMoves) == 0:
        col,row= computer_play(board)
        flipList=changeTrain(board,validMoves,color,row,col,neighbors)
        place_move(color,row,col,coordinates,flipList)
        playerScore,computerScore= scoreCard(flipList,playerScore,computerScore,color)
        print(playerScore)
        print(computerScore)
        isValidMove(board,row,col,color,flipList)
        board= board_update(flipList,color,board)

if __name__ == '__main__':
  main()
