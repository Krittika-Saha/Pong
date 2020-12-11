from turtle import Turtle
from time import sleep

class Ball(Turtle):

  def __init__(self, width, height, color):
    """Creates pong ball"""
    super().__init__()
    self.up()
    self.shape('circle')
    self.color('white')

  def move(self):
    """Moves ball"""
    x = self.xcor() + 10
    y = self.ycor() + 10
    self.goto(x, y)
    sleep(0.1)

