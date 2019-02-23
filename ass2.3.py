#ass2.3.py
#
#function that draws a grid made of pluses and minuses that is r rows by c columns
#usage: ???
#   %python ass2.3.py rows and columns
#
#Helen Gao, 7-2-2018 by 9:59am

def grid(rows, columns): #defining a function called grid
    plusminus = "+----" #making a local variable called plusminus that is '+----' because that is the repeating portion of the grid
    verticalbar = "|    " #making a local variable called verticalbar that is a vertical bar followed by four spaces because that is the repeating portion of the grid
    return((plusminus * columns + "+\n" + 4* (verticalbar * columns + "|\n")) * rows + plusminus * columns + "+") #used return to avoid printing in the function. (forgot to do this at first and used print instead, which gave me a lot of trouble later, especially since i was using multiple lines of print.) multiplied plusminus by the imput columns so that there would be enough columns, then added a plus at the end to complete the grid and started a new line. used concatenation so that there wouldn't be a space between this line and the next (this was actually the part that gave me the most trouble, went to joe's section on thursday to get help). the next line used the verticalbar variable which was also multiplied by columns to create enough bars and had a vertical bar with a new line at the end, but this part was multiplied by four because there were four lines of vertical bars. this whole thing was multiplied by the parameter rows so that the grid would repeat however many rows were inputted. finally added another plusminus part at the end to close the grid but didn't use a new line because it wasn't needed at the end of the grid.

print(grid(2, 2)) #part a of the assignment, prints grid with 2 rows and 2 columns

print(grid(4, 4)) #part b of the assignment, prints grid with 4 rows and 4 columns

#went to joe's section/office hours on thursday to get some help (mostly with getting the return function to work out)