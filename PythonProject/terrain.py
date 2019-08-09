import turtle
import random

# TODO: decide off screen behaviour
def getYPoint(x):
  """ Finds the y point of the line given an x """
  global coords
  afterX = 0
  afterY = 0
  for coord in coords:
    if x == coord[0]:
      return coord[1]
    beforeX = afterX
    beforeY = afterY
    afterX = coord[0]
    afterY = coord[1]
    if x > beforeX and x < afterX:
      break
  # proportion of distance on the x axis * difference in Y + y starting point
  return ((x-beforeX)/(afterX-beforeX))*(afterY-beforeY)+beforeY

def aboveLine(x,y):
  """ Takes point coordinates and returns boolean whether the point is above the line."""
  yPoint = getYPoint(x)
  if y > yPoint:
    return True
  else:
    return False

def onPad(x):
  """ Returns whether the lander is on the pad """
  global pad
  tolerance = 20
  if x > pad.xcor() - tolerance and x < pad.xcor() + tolerance:
    return True
  else:
    return False

WIDTH = 400
HEIGHT = 400

# All figures are proportional to the width and height
STARTX = -int(WIDTH/2)
STARTY = -int(HEIGHT*0.375)
MOVEMENT = HEIGHT/20
LOWER_BOUNDS = int(STARTY+1.5*MOVEMENT)
UPPER_BOUNDS = int(STARTY-1.5*MOVEMENT)
PAD_LIMITS = WIDTH/2-10

turtle.Screen().setup(WIDTH,HEIGHT) 
turtle.Screen().bgpic("sky.jpg")

numPads = 1
coords = []

# Initiate turtle
pad = turtle.Turtle()
pad.speed(0)
pad.shape("square")
#pad.turtlesize(2,0.5)
pad.hideturtle()
pad.penup()

pad.goto(STARTX,STARTY)
coords.append((STARTX,STARTY))
pad.pendown()
pad.fillcolor('lightgray')
pad.begin_fill()
# Proceedurally generate terrain randomly
while pad.xcor() < WIDTH/2:
  newX = pad.xcor() + random.randint(int(WIDTH/40),int(WIDTH/8))
  if pad.ycor() > LOWER_BOUNDS or pad.ycor() < UPPER_BOUNDS:
    newY = random.randint(UPPER_BOUNDS,LOWER_BOUNDS)
  else:
    newY = pad.ycor() + random.randint(-MOVEMENT,MOVEMENT)
  coords.append((newX,newY))
  pad.goto(newX,newY)
pad.goto(WIDTH/2,-HEIGHT/2)
pad.goto(-WIDTH/2,-HEIGHT/2)
pad.end_fill()

# Place landing pad
pad.penup()
padX = random.randint(-PAD_LIMITS,PAD_LIMITS)
pad.goto(padX,getYPoint(padX))
pad.setheading(0)
pad.showturtle()