#import statements 
import turtle as trtl
import random as rand
import time

#background
wn = trtl.Screen()
wn.bgpic("NAWS2.gif")

#general set-up (establish turtles + lists(also picks random index of lists for meat, resp_list, and alphabetti))
meat = ["My cat", "Regular ingriedients", "Swag"]
resp_list = ["Why?", "Stop.", "???: You fool.", ":/", "???: Alright, that's it."]
alphabetti = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letter = rand.randrange(len(alphabetti))
meatball = rand.randrange(len(meat))
response = rand.randrange(len(resp_list))
gif_list = ["amongus1.gif","amongus2.gif"]
drawer2 = trtl.Turtle()
drawer = trtl.Turtle()
lefto = trtl.Turtle()
sus = trtl.Turtle()
g = trtl.Turtle()
spag = trtl.Turtle()
amogus = trtl.Turtle()
screen = trtl.Turtle()

#old lady set-up
wn.addshape("grandmother-dancing.gif")
g.shape("grandmother-dancing.gif")
g.penup()
g.goto(0,-50)

#user set-up
trtl.hideturtle()
wn.addshape("user5.gif")
trtl.shape("user5.gif")
trtl.penup()
trtl.goto(500,-100)
trtl.showturtle()
trtl.penup()
trtl.goto(300,-100)

#suspicious stew set-up
wn.addshape("sus_stew2.gif")
sus.shape("sus_stew2.gif")
sus.penup()
sus.goto(-165,-200)

#spaghetti set-up
wn.addshape("spaghetti2.gif")
spag.shape("spaghetti2.gif")
spag.penup()
spag.goto(0,-240)

#changes bg to include a white spot + writes the letter that the user has to press (spaghetti route)
def button():
  wn.bgpic("new.gif")
  drawer2.hideturtle()
  drawer2.penup()
  drawer2.goto(-20,-350)
  drawer2.pendown()
  drawer2.pencolor("white")
  font2 = ("Comic Sans MS", 70)
  drawer2.write(alphabetti[letter],font=font2)

#ends spaghetti route
def spag_end():
  black_screen()
  time.sleep(2)
  wn.bye()

#leftover set-up
wn.addshape("leftovers2.gif")
lefto.shape("leftovers2.gif")
lefto.penup()
lefto.goto(165,-200)

#set-up black screen from suspicious stew
screen.hideturtle()
screen.shape("square")
screen.color("black")

#turns the screen black (game ending sequence)
def black_screen():
  screen.showturtle()
  screen.shapesize(50)
  drawer.clear()
  drawer2.clear()
  drawer2.hideturtle()

#flashes red then turns black (this is the death sequence)
def death():
  screen.color("red")
  black_screen()
  screen.color("black")
  black_screen()
  time.sleep(2)
  wn.bye()

#amongus gif set-up
def gif():
  image_num = 0
  #this cycles through the images making the gif look animated
  while image_num <= 1:
    wn.addshape(gif_list[image_num])
    amogus.shape(gif_list[image_num])
    image_num = image_num + 1
    time.sleep(0.5)

#text setup
drawer.hideturtle()
drawer.penup()
drawer.goto(-400,320)
drawer.pendown()
drawer.color("Black")
font = ("Comic Sans MS", 20)

#arrow key functions
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
  time.sleep(2.5)
  drawer.clear()

#hides all other menu items to prevent them from being clicked
def hide_items():
  drawer.clear()
  sus.hideturtle()
  spag.hideturtle()
  lefto.hideturtle()

#instructions for user
drawer.write("Click on a food to choose it. Move around using arrow keys.",font=font)

#if the user is dumb and clicks the old lady
def g_clicked(x,y):
  drawer.clear()
  drawer.write("...", font=font)
  next_text()
  drawer.write(resp_list[response], font=font)
  #two if statements for two possible responses from the old lady (I have to add two because for whatever reason neither the "or" or "and" type of if statement work)
  if resp_list[response] == "???: You fool.":
    time.sleep(2)
    death()
  if resp_list[response] == "???: Alright, that's it.":
    time.sleep(3)
    death()
  
#this storyline activates when suspicious stew is clicked
def sus_clicked(x,y):
  hide_items()
  drawer.write("Which flavor?", font=font)
  yeet = input("Which flavor?")
  yeet = yeet.lower()
  next_text()
  drawer.write("You: I would like " + yeet + " flavored stew.",font=font)
  next_text()
  drawer.write("???: Ah, it doesn't matter.",font=font)
  next_text()
  drawer.write("You: Oh.",font=font) 
  next_text()
  drawer.write("You take a long slurp of the suspicious stew. It is very suspicious.",font=font)
  next_text()
  drawer.write("Are you ready?", font=font)
  amongus = input("Are you ready (yes or no)?")
  amongus = amongus.lower()

  #user input for yes or no activates alternate storylines
  if amongus == "yes":
    screen.showturtle()
    screen.shapesize(50)
    drawer.clear()
    time.sleep(2)
    for i in range(5):
      gif()
    wn.bye()
  
  elif amongus == "no":
    print("Don't come back :)")
    wn.bye()
  #if user enters anything else, the game ends 
  else:
    print("Follow instructions next time, you clown.")
    wn.bye()

#this storyline is activated when spaghetti and meatballs are clicked
def spag_clicked(x,y):
  hide_items() 
  drawer.write("???: Guess what's in the meatballs!", font=font)
  next_text()
  drawer.write("You: What? What's in it?", font=font)
  next_text()
  drawer.write("???: " + meat[meatball]+ ", of course.", font=font)
  next_text()
  drawer.write("You: Uhhhh....", font=font)
  next_text()
  drawer.pencolor("red")
  drawer.write("L E A V E", font=font)
  button()

#this storyline is activated when leftovers are clicked
def lefto_clicked(x,y):
  hide_items()
  drawer.write("???: Ah, the leftovers!", font=font)
  next_text()
  drawer.write("You: Leftovers of what exactly?", font=font)
  next_text()
  drawer.write("???: Ahaha, try it and find out.. :)", font=font)
  next_text()
  adj = input("Give me an adjective lol")
  drawer.write("You: Uhm, ok..? Looks " +adj+ " I guess?", font=font)
  next_text()
  drawer.write("It was " +adj+ "." "Too " +adj+ ".", font=font)
  next_text()
  death()

#to activate storylines when item is clicked
sus.onclick(sus_clicked)
spag.onclick(spag_clicked)
lefto.onclick(lefto_clicked)
g.onclick(g_clicked)

#arrow keys
wn.onkeypress(forward,"Up")
wn.onkeypress(backward,"Down")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")

#activates the end of the route when the letter on the screen is pressed (spaghetti route)
wn.onkeypress(spag_end,alphabetti[letter])

#detects keyboard + mouse input and keeps the game running 
wn.listen()
wn.mainloop()