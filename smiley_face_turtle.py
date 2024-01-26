import turtle
import time

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle named 'smiley'
smiley = turtle.Turtle()
smiley.shape("circle")  # Set turtle shape to a circle (for the face)
smiley.color("yellow")   # Set turtle color to yellow
smiley.speed(2)          # Set turtle drawing speed

# Function to draw the smiley face
def draw_smiley():
    # Move to the starting position for the face
    smiley.penup()
    smiley.goto(0, -150)
    smiley.pendown()
    
    # Draw the face (a filled yellow circle)
    smiley.begin_fill()
    smiley.circle(150)
    smiley.end_fill()

    # Draw the left eye (a filled black circle)
    smiley.penup()
    smiley.goto(-40, 40)
    smiley.pendown()
    smiley.color("black")
    smiley.begin_fill()
    smiley.circle(20)
    smiley.end_fill()

    # Draw the right eye (a filled black circle)
    smiley.penup()
    smiley.goto(40, 40)
    smiley.pendown()
    smiley.color("black")
    smiley.begin_fill()
    smiley.circle(20)
    smiley.end_fill()

    # Draw the smile (a semicircle)
    smiley.penup()
    smiley.goto(-70, -20)
    smiley.pendown()
    smiley.right(90)
    smiley.circle(70, 180)

# Animate the smiley face
for _ in range(2):
    draw_smiley()      # Call the draw_smiley function
    time.sleep(1)      # Pause for 1 second
    smiley.clear()      # Clear the drawing

# Close the turtle graphics window when clicked
screen.exitonclick()
