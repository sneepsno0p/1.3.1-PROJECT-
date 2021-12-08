import turtle as player
player.penup()
player.shape("triangle")
player.shapesize(2)
#arrow key functions + arrow key stop-moving functions
def forward():
  player.forward(10)

def backward():
  player.backward(10)

def left():
  player.left(10)

def right():
  player.right(10)

screen = player.Screen()
#these keybind the functions to corresponding arrow keys (onkeypress makes the function run for
# as long as the arrow key is pressed) 
screen.onkeypress(forward, "Up")
screen.onkeypress(backward, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

screen.listen()
screen.mainloop()
