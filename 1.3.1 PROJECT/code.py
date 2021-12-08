import turtle as trtl
import random as rand
import time

#turtle Set-up
turtle_list = ["left", "sus", "spag"]
wn = trtl.Screen()
drawer = trtl.Turtle()
left = trtl.Turtle()
sus = trtl.Turtle()
g = trtl.Turtle()
spag = trtl.Turtle()
screen = trtl.Turtle()

screen.hideturtle()
wn.addshape("spaghetti2.gif")
spag.shape("spaghetti2.gif")
wn.addshape("user5.gif")
trtl.shape("user5.gif")
wn.addshape("leftovers2.gif")
left.shape("leftovers2.gif")
wn.addshape("grandmother-dancing.gif")
g.shape("grandmother-dancing.gif")
wn.addshape("sus_stew2.gif")
sus.shape("sus_stew2.gif")
screen.shape("square")
screen.color("black")

#background shows up early
wn.bgpic("NAWS2.gif")

#text setup
drawer.penup()
drawer.goto(-200,210)
drawer.pendown()
drawer.color("white")
font = ("Comic Sans MS", 20)
drawer.hideturtle()

#arrow key functions + arrow key stop-moving functions
trtl.penup()
def forward():
  trtl.setheading(90)
  trtl.forward(10)

def backward():
  trtl.setheading(270)
  trtl.forward(10)

def left():
  trtl.setheading(180)
  trtl.forward(10)

def right():
  trtl.setheading(0)
  trtl.forward(10)

#to clear text
def next_text():
  time.sleep(3)
  drawer.clear()
sus.hideturtle()
sus.penup()
sus.goto(-150,-200)
sus.showturtle()

drawer.write("Click on a food to choose it.",font=font)

def sus_clicked(x,y):
  drawer.clear()
  sus.hideturtle()
  drawer.write("Which flavor?", font=font)
  yeet = input("Which flavor?")
  next_text()
  drawer.write("You: I would like " + yeet + " flavored stew.",font=font)
  next_text()
  drawer.write("???: Ah, it doesn't matter",font=font)
  next_text()
  drawer.write("You: Oh.",font=font) 
  next_text()
  drawer.write("You take a long, careful slurp of the suspicious stew. It is very suspicious.",font=font)
  next_text()
  drawer.write("Y or N?", font=font)
  f = input("Y or N?")

  if f == "Y":
    screen.showturtle()
    screen.shapesize(50)
    time.sleep(6)
    screen.hideturtle()
    wn.bgpic("user5.gif")



#epic = {"ds":"e"}
#print(epic["ds"])


#these keybind the functions to corresponding arrow keys (onkeypress makes the function run for as long as the arrow key is pressed) 
sus.onclick(sus_clicked)
wn.onkeypress(forward,"Up")
wn.onkeypress(backward,"Down")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")
wn.listen()
wn.mainloop()

