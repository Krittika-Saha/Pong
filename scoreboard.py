from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color('white')
    self.up()
    self.hideturtle()
    self.l_score = 0
    self.r_score = 0
    self.speed('fastest')
    self.winner = ''
    self.l_name = ''
    self.r_name = ''

  def update(self):
    """Updates the scoreboard"""
    self.clear()
    self.goto(-100, 200)
    self.write(self.l_score, align='center', font=('Courier', 80, "normal"))
    self.goto(100, 200)
    self.write(self.r_score, align='center', font=('Courier', 80, "normal"))

  def l_point(self):
    """Gives a point to the left player"""
    self.l_score += 1
    self.update()

  def r_point(self):
    """Gives a point to the right player"""
    self.r_score += 1
    self.update()

  def declare_winner(self):
    """Prints the name of the winner"""
    self.goto(0, 0)
    self.write(self.winner, align='center', font=('Helvetica', 80, "normal"))
