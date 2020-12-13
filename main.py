from turtle import Turtle, Screen
from paddle import Paddle
from time import sleep
from ball import Ball
from scoreboard import Scoreboard
from stadium import Stadium

timmy = Turtle()
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
scoreboard = Scoreboard()
# scoreboard.l_name = screen.textinput("Left Player Name", "Enter your name: ")
# scoreboard.r_name = screen.textinput("Right Player Name", "Enter your name: ")
stadium = Stadium()

paddle_1 = Paddle(20, 100, 'white', (350, 0))
paddle_2 = Paddle(20, 100, 'white', (-350, 0))
screen.listen()
screen.onkeypress(paddle_1.move_fd, 'Up')
screen.onkeypress(paddle_1.move_bk, 'Down')
screen.onkeypress(paddle_2.move_fd, 'w')
screen.onkeypress(paddle_2.move_bk, 's')
ball = Ball(1, 1, 'white')
scoreboard = Scoreboard()
scoreboard.update()
game_is_on = True
while game_is_on:
  ball.move_r()
  screen.update()
  if paddle_2.ycor() > 240:
    paddle_2.goto(-350, 240)
  elif paddle_2.ycor() < -240:
      paddle_2.goto(-350, -240)
  elif paddle_1.ycor() > 240:
      paddle_1.goto(350, 240)
  elif paddle_1.ycor() < -240:
      paddle_1.goto(350, -240)
  #Detect collision with wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()
    ball.sleep_timer /= 2


  #Detect collisions with paddle
  if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
    ball.bounce_x()
    ball.sleep_timer /= 2

  #Detect when ball is out of bounds
  if ball.xcor() < -380:
    ball.reset_position()
    scoreboard.r_point()

  elif ball.xcor() > 380:
    ball.reset_position()
    scoreboard.l_point()

  else:
    continue

  

  








screen.exitonclick()