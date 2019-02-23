#pentagram.py
#
#function that draws a pentagle with the parameters turtle, edge length, and pen width
#usage: ???
#   % python pentagram.py t, edgeLen, penWidth
#
#Helen Gao, 7-9-2018 by 11am
import turtle #import the turtle library
bob = turtle.Turtle() #create a turtle named bob
def draw_pentagram(t, edgeLen, penWidth): #the function takes the parameters t for turtle, edgeLen for the pixel length of each side of the pentagram, and penWidth for the pixel width of the pen that the turtle is drawing with to create a pentagram
    for i in range(5): #since a pentagram has 5 sides, this loop runs 5 times
        t.pensize(penWidth) #sets the turtle's pensize to a given pen width
        t.fd(edgeLen) #moves the turtle forward the given edge length
        t.rt(144) #turns the turtle 144 degrees to the right. the middle of the pentagram is a regular pentagon, which has interior degrees of 540/5=108 degrees. the angles adjacent to each of these degrees form linear pairs, so each of these measure 72 degrees. the points on the pentagram are formed by isosceles triangles, so the measure of the interior angle of the pentagram is 180-(72*2)=36 degrees. since the turtle turns on the outside, it turns 180-36=144 degrees to the right
    t.ht() #hiding the turtle now. bye turtle. we still love him though
draw_pentagram(bob, 500, 20) #draws the pentagram using the turtle bob, an edge length of 200, and a pen width of 20
turtle.mainloop() #the window stays open for our viewing pleasure