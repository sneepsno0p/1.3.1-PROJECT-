import turtle
turtle.penup()

#arrow key functions + arrow key stop-moving functions
def forward():
  turtle.forward(10)

def backward():
  turtle.backward(10)

def left():
  turtle.left(10)

def right():
  turtle.right(10)

screen = turtle.Screen()
#these keybind the functions to corresponding arrow keys (onkeypress makes the function run for
# as long as the arrow key is pressed) 
screen.onkeypress(forward, "Up")
screen.onkeypress(backward, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

screen.listen()
screen.mainloop()
