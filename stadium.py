from turtle import Turtle 

class Stadium(Turtle):

  def __init__(self):
    super().__init__()
    self.pencolor('grey')
    self.pensize(5)
    self.speed('fastest')
    self.hideturtle()
    self.left(90)
    self.up()
    self.goto(0, -300)
    for i in range(15):
      self.down()
      self.fd(20)
      self.up()
      self.fd(20)