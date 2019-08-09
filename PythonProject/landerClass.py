import turtle
import time

turtle.Screen().register_shape("lander.png")
turtle.Screen().register_shape("thrusters.png")
turtle.Screen().register_shape("crashed.png")
turtle.Screen().register_shape("left.png")
turtle.Screen().register_shape("right.png")
turtle.Screen().register_shape("left-thrust.png")
turtle.Screen().register_shape("right-thrust.png")

class landerClass(turtle.Turtle):
  def __init__(self):
    super().__init__(self)
    self.hideturtle()
    self.shape("lander.png")
    self.penup()
    self.speed(0)
    self.setheading(90)
    self.goto(0,200)
    self.speed(6)
    self.showturtle()
  
  def toggleThrust(self):
    if self.active:
      if self.thrusters:
        self.shape("lander.png")
        self.thrusters = False
      else:
        self.shape("thrusters.png")
        self.thrusters = True
  
  def right(self):
    if self.active: 
      super().right(5)
      if self.thrusters:
        self.shape("right-thrust.png")
      else:
        self.shape("right.png")
      time.sleep(0.1)
      if self.active:
        if self.thrusters:
          self.shape("thrusters.png")
        else:
          self.shape("lander.png")
  
  def left(self):
    if self.active: 
      super().left(5)
      if self.thrusters:
        self.shape("left-thrust.png")
      else:
        self.shape("left.png")
      time.sleep(0.1)
      if self.active:
        if self.thrusters:
          self.shape("thrusters.png")
        else:
          self.shape("lander.png")

  def landed(self):
    self.active = False
    time.sleep(0.01)
    self.shape("lander.png")
    
  def crash(self):
    self.active = False
    time.sleep(0.01)
    self.shape("crashed.png")
  
  ACCELERATION = 0.01
  THRUST = 0.05
  thrusters = False
  active = True
  yVel = 2
  xVel = 0
  fuel = 100