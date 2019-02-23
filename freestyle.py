#freestyle.py
#
#function that draws something interesting using the turtle, incorporating at least two new features from the turtle library that we didn't discuss in class
#usage: ???
#   % python freestyle.py color (as hex codes)
#
#Helen Gao, 7-9-2018 by 11am

import turtle #import the turtle library
bob = turtle.Turtle() #create a turtle named bob
bob.penup() #raising the pen so that bob doesn't draw when we set bob's position
bob.setpos(-500, 350) #using the new setpos function to change bob's position to the coordinates (-500, 350) so that the whole image can be displayed on my screen
bob.pendown() #putting the pen back down so that bob can draw

def gradient(color): #creating a function called gradient that has a color's hex code as a parameter
    bob.color(color) #using the new function color to set the pen to the given color
    bob.begin_fill() #using the new function fill to fill the next part of this function with a given color
    for i in range(2): #for loop that draws half a rectangle. it runs twice since the whole shape is a full rectangle
        bob.fd(1050) #bob moves forward the length 1050 pixels to form the first side of the rectangle
        bob.rt(90) #bob turns 90 degrees right
        bob.fd(20) #bob moves forward the width 20 pixels to form the second side of the rectangle
        bob.rt(90) #bob turns 90 degrees right again
    bob.end_fill() #bob fills the above rectangle
    bob.rt(90) #bob turns 90 degrees right so that he's pointing down again
    bob.fd(20) #bob moves forward 20 pixels to be at the bottom left corner of the rectangle
    bob.lt(90) #bob turns 90 degrees left to point right again

gradient("#7dbfd5") #these are all rectangles of slightly different shades of blue. i used gimp 2's color picker tool to find the hex codes of the colors in the original gradient
gradient("#7cbfd0") #this is only the second color. there are 30 more but i can't use a loop since the arguments are all different colors
gradient("#7bbcd0")
gradient("#78b8d3")
gradient("#78b6cf")
gradient("#75b2cf")
gradient("#75aec9")
gradient("#73aac9")
gradient("#72a7c6")
gradient("#6fa4c4")
gradient("#6da3bf")
gradient("#699dc4")
gradient("#6a9cbd")
gradient("#679cbc")
gradient("#6296bb")
gradient("#6294b9")
gradient("#5f91b6")
gradient("#5c8db6")
gradient("#5c8bb7")
gradient("#5c87b4")
gradient("#5a85b2")
gradient("#5a83b1")
gradient("#5780ac")
gradient("#547da9")
gradient("#557ba8")
gradient("#5378ac")
gradient("#5075a2")
gradient("#4d71a1")
gradient("#4f6ea4")
gradient("#4c6ba4")
gradient("#4d6ba1")
gradient("#49679d")

bob.penup() #bob's pen goes up again so that he doesn't draw when we start drawing the crown
bob.setpos(-400, 100) #repositioning bob to the coordinates x=-400, y=100
bob.pendown() #bob's pen goes down so he can start drawing again

bob.color("#ffffff") #setting the color to white for the crown
bob.begin_fill() #the next part is going to be filled white

bob.fd(157) #this next part is the 9 part of the crown. i used gimp again to find all the side lengths and angle measures. since they're almost all different, i still can't use a loop
bob.rt(50)
bob.fd(275)
bob.lt(90)
bob.fd(36)
bob.lt(90)
bob.fd(185)
bob.rt(80)
bob.fd(304)
bob.rt(100)
bob.fd(304)
bob.rt(80)
bob.fd(339)
bob.rt(50)
bob.fd(159)
bob.rt(50)
bob.fd(400)
bob.end_fill() #the 9 is filled

bob.penup() #bob's pen goes up again so that he doesn't draw when he moves to draw the next shape

bob.rt(130) #bob moves over to the middle of the 9
bob.fd(436)
bob.pendown() #bob's pen goes back down to fill in the center of the 9


#10
bob.color("#679cbc") #bob uses a new color from the gradient now
bob.begin_fill() #the next part is filled with the above color
bob.rt(50) #bob draws a triangle
bob.fd(64)
bob.rt(130)
bob.fd(82)
bob.rt(130)
bob.fd(64)
bob.rt(100) #bob retraces his steps to where the second triangle starts
bob.fd(64)
bob.end_fill() #bob fills the triangle

bob.color("#5f91b6")
bob.begin_fill()
bob.rt(80)
bob.fd(64)
bob.rt(100)
bob.fd(64)
bob.rt(130)
bob.fd(82)
bob.end_fill() #bob fills the second triangle

bob.penup() #bob's pen goes up so he doesn't move while repositioning
bob.bk(82) #using the new back function to retrace bob's steps and move over to draw last part of the crown
bob.lt(50)
bob.fd(64)
bob.rt(50)
bob.fd(279)

bob.pendown() #bob's pen goes down to draw the last part
bob.color("#ffffff") #this part is also white
bob.begin_fill() #the next part will be filled white
for i in range(2): #since this part is a parallelogram, half of it can be run twice
    bob.fd(157)
    bob.rt(130)
    bob.fd(401)
    bob.rt(50)
bob.end_fill() #bob fills in the parallelogram to finish the crown
bob.hideturtle() #hiding bob now. bye bob. we love him though
turtle.mainloop() #the window stays open for our viewing pleasure

#note: a big part of why this is so complicated is that i originally only programmed it to draw the crown itself, without the gradient. since i wanted to make the program look cool while drawing said crown, i made bob draw everything as continuously as possible rather than breaking the figure up into individual parallelograms. but when i was done i decided i wanted to be true to the original, so i had to modify the diamond in the middle of the 9 so that it had part of the gradient in the colors. i did take a look at the site that professor parker linked, but i didn't really understand any of the functions or libraries that the examples used. so, the first 50 lines happened. sorry to whoever has to grade this. here's a link to a video of the drawing process that has the gradient portion sped up x5: http://syncos-biggest-fan.tumblr.com/post/175621597812