from turtle import Turtle, Screen
from paddle import Paddle
from time import sleep
from ball import Ball

timmy = Turtle()
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')

paddle_1 = Paddle(20, 100, 'white', (350, 0))
paddle_2 = Paddle(20, 100, 'white', (-350, 0))
screen.listen()
screen.onkey(paddle_1.move_fd, 'Up')
screen.onkey(paddle_1.move_bk, 'Down')
screen.onkey(paddle_2.move_fd, 'w')
screen.onkey(paddle_2.move_bk, 's')
ball = Ball(1, 1, 'white')


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
  elif ball.xcor() > 380:
    ball.reset_position()
  else:
    continue

  








screen.exitonclick()


# from turtle import Screen, Turtle
# from paddle import Paddle
# from ball import Ball
# from scoreboard import Scoreboard
# import time

# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=800, height=600)
# screen.title("Pong")
# screen.tracer(0)

# r_paddle = Paddle((350, 0))
# l_paddle = Paddle((-350, 0))
# ball = Ball()
# scoreboard = Scoreboard()

# screen.listen()
# screen.onkey(r_paddle.go_up, "Up")
# screen.onkey(r_paddle.go_down, "Down")
# screen.onkey(l_paddle.go_up, "w")
# screen.onkey(l_paddle.go_down, "s")

# game_is_on = True
# while game_is_on:
#     screen.update()
#     ball.move()

#     #Detect collision with wall
#     if ball.ycor() > 280 or ball.ycor() < -280:
#         ball.bounce_y()

#     #Detect collision with paddle
#     if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
#         ball.bounce_x()