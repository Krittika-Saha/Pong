from turtle import Turtle, Screen
from paddle import Paddle
from time import sleep
from ball import Ball
from scoreboard import Scoreboard

timmy = Turtle()
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
scoreboard = Scoreboard()
scoreboard.l_name = screen.textinput("Left Player Name", "Enter your name: ")
scoreboard.r_name = screen.textinput("Right Player Name", "Enter your name: ")


paddle_1 = Paddle(20, 100, 'white', (350, 0))
paddle_2 = Paddle(20, 100, 'white', (-350, 0))
screen.listen()
screen.onkey(paddle_1.move_fd, 'Up')
screen.onkey(paddle_1.move_bk, 'Down')
screen.onkey(paddle_2.move_fd, 'w')
screen.onkey(paddle_2.move_bk, 's')
ball = Ball(1, 1, 'white')
scoreboard = Scoreboard()

scoreboard.update()
while True:
  ball.move_r()
  screen.update()
  
  
  #Detect collision with wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  #Detect collisions with paddle
  if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
      ball.bounce_x()

  #Detect when ball is out of bounds
  if ball.xcor() < -380:
    ball.reset_position()
    scoreboard.r_point()
    if scoreboard.r_score == 5:
      scoreboard.winner == scoreboard.r_name
      break
  elif ball.xcor() > 380:
    ball.reset_position()
    scoreboard.l_point()
    if scoreboard.l_score == 5:
      scoreboard.winner == scoreboard.l_name
      break
  else:
    continue
scoreboard.declare_winner()
  

  








screen.exitonclick()