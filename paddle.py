from turtle import Turtle

class Paddle(Turtle):

  def __init__(self, width, height, color, cor_tuple):
    """Creates a pong paddle"""
    super().__init__()

    self.up()
    self.shape('square')
    self.turtlesize(stretch_wid = 1, stretch_len = 5)
    self.speed('fastest')
    self.color(color)
    self.goto(cor_tuple)
    self.left(90)
    
  
  def move_fd(self):
    """Moves paddle forward"""
    self.fd(20)

  def move_bk(self):
    """Moves paddle backward"""
    self.bk(20)




  