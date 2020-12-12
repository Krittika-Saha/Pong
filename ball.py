from turtle import Turtle
from time import sleep

class Ball(Turtle):

  def __init__(self, width, height, color):
    """Creates pong ball"""
    super().__init__()
    self.up()
    self.shape('circle')
    self.color('white')
    self.x = 10
    self.y = 10

  def move(self):
    """Moves ball"""
    x = self.xcor() + self.x
    y = self.ycor() + self.y
    self.goto(x, y)
    sleep(0.1)

  def bounce_y(self):
    """Ball bounces back from wall"""
    self.y *= -1

  def bounce_x(self):
    """Ball bounces off paddle"""
    self.x *= -1

