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
  ball.move()
  screen.update()

  #Detect collision with wall
  if ball.ycor() > 300 or ball.ycor() < -300:
    ball.bounce()








screen.exitonclick()