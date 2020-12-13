from turtle import Turtle
from time import sleep

class Ball(Turtle):

  def __init__(self, width, height, color):
    """Creates pong ball"""
    super().__init__()
    self.up()
    self.shape('circle')
    self.color('white')
    self.turtlesize(stretch_wid = 0.5, stretch_len = 0.5)
    self.x = 10
    self.y = 10
    self.speed('fastest')
    self.sleep_timer = 0.1

  def move_r(self):
    """Moves ball towards the right paddle"""
    x = self.xcor() + self.x
    y = self.ycor() + self.y
    self.goto(x, y)
    sleep(self.sleep_timer)

  def bounce_y(self):
    """Ball bounces back from wall"""
    self.y *= -1

  def bounce_x(self):
    """Ball bounces off paddle"""
    self.x *= -1

  def reset_position(self):
    """Resets balls position in the center position"""
    self.goto(0,0)
    self.bounce_x()
