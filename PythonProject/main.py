#!/bin/python3
import terrain
from landerClass import landerClass
from turtle import Screen
from math import sin, cos, radians
lander = landerClass()
Screen().onkey(lander.left, "Left")
Screen().onkey(lander.right, "Right")
Screen().onkey(lander.toggleThrust, "Space")
Screen().listen             ()
while True:
  lander.yVel += lander.ACCELERATION
  lander.sety(lander.ycor() - lander.yVel)
  lander.setx(lander.xcor() + lander.xVel)
  if lander.thrusters:
    heading = radians(lander.heading())
    lander.yVel -= lander.THRUST * sin(heading)
    lander.xVel += lander.THRUST * cos(heading)
if terrain.onPad(lander.xcor()) and lander.yVel < 2:
  lander.landed()  
else:
  lander.crash()