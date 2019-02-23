#hopscotch.py
#
#function that draws a hopscotch court with the parameters for a turtle, edge length, and pen width
#usage: ???
#   % python hopscotch.py t, edgeLen, penWidth
#
#Helen Gao, 7-9-2018 by 11am

import turtle #import the turtle library
bob = turtle.Turtle() #create a turtle named bob
def square(t, edgeLen): #this function takes the parameters t for turtle and edgeLen for the edge length of the square
    for i in range(4): #since it is a square, drawing one side can be repeated four times
        t.fd(edgeLen) #the turtle moves forward the designated edge length
        t.rt(90) #the turtle turns 90 degrees in preparation for drawing the next edge length
def twosquares(t, edgeLen): #this function draws two square side by side using the above square function and uses the same parameters
    square(t, edgeLen) #drawing a square
    t.fd(edgeLen) #moves to the top right corner of the first square so the turtle can start drawing the next square
    square(t, edgeLen) #draws the second square
def threesquares(t, edgeLen): #this function draws a square on top of two squares using the square function and the twosquares function
    square(t, edgeLen) #draws the top square
    t.rt(90) #turns the turtle so it faces downwards
    t.fd(edgeLen) #moves down the length of the square so the turtle is at the bottom left corner of the first square
    t.lt(90) #turtle turns left 90 degrees so it faces to the right
    t.bk(edgeLen/2) #turtle moves back 1/2 the length of the side length so that the twosquares function will be centered properly
    twosquares(t, edgeLen) #turtle draws two squares
    t.rt(90) #turtle turns so that it's facing downwards
    t.fd(edgeLen) #turtle moves down the center of the two triangles
    t.lt(90) #turtle turns left so that it faces to the right
    t.bk(edgeLen/2) #turtle moves back so that it will be centered when it draws the single square
def hopscotch_court(t, edgeLen, penWidth): #this function creates the hopscotch court using the parameters t for turtle, edgeLen for edge length, and penWidth for pen size
    t.penup() #the turtle's pen goes up so it doesn't draw when repositioning
    t.setpos(-edgeLen/2, edgeLen*3) #the turtle's position is set so that the starting point is half the length of the edge to the left (because the first square is a full edge length long, this will center it) and since the hopscotch court is six edge lengths tall, placing it at a y-value of three edge lengths will also center the court vertically
    t.pendown() #the turtle's pen goes down to start drawing
    t.pensize(penWidth) #sets the pen size to the given pen width
    for i in range(2): #since the hopscotch court has two sets of three squares, the threesquares function can be run twice
        threesquares(t, edgeLen) #runs threesquares with the parameters t and edgeLen
    square(t, edgeLen) #draws the seventh square after finishing the first 2*3=6 squares
    t.rt(90) #the turtle turns right so that it faces down
    t.fd(edgeLen) #the turtle moves forward so that it is at the bottom left corner of the seventh square
    t.lt(90) #the turtle turns left so that it faces right in preparation for drawing the next square
    square(t, edgeLen) #the turtle draws the last square
    t.ht() #hiding the turtle now. bye turtle. we still love him though
hopscotch_court(bob, 75, 6) #draws the hopscotch court with the turtle bob, each square having edges of length 75 pixels, and the width of the lines being 6 pixels
turtle.mainloop() #the window stays open for our viewing pleasure

#note: got the ideas for repeated square functions and centering the drawing at joe's thursday section