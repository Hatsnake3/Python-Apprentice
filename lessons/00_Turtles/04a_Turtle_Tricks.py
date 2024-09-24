"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=300, height=300)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina
                 


# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()

... # Your code here

tina.speed(1)
tina.forward(100)
tina.left(135)
tina.forward(100)
tina.left(90)
tina.forward(100)
tina.left(135)
tina.forward(100)


tina.begin_fill()
tina.fillcolor('green')
tina.end_fill()




turtle.exitonclick()                    # Close the window when we click on it
