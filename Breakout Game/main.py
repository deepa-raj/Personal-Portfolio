import time
from turtle import Turtle, Screen
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard
from paddle import Paddle

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

STARTING_POSITION = (0, -250)

class BreakOut:
    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.title("Breakout Game")
        self.screen.tracer(0)
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.paddle = Paddle(position=STARTING_POSITION)
        self.ball = Ball()
        self.outline()
        self.building_bricks()

        self.moving_left = False
        self.moving_right = False

        self.moving_paddle()
        self.screen.listen()
        self.screen.onkeypress(self.move_left, "Left")
        self.screen.onkeypress(self.move_right, "Right")
        self.screen.onkeyrelease(self.stop_move, "Left")
        self.screen.onkeyrelease(self.stop_move, "Right")

        self.game_on = True
        self.score_board = Scoreboard()
        while self.game_on:
            self.screen.update()
            time.sleep(self.ball.move_speed)
            self.ball.move()

            # Collision with wall
            if self.ball.xcor() < -460 or self.ball.xcor() > 460:
                self.ball.bounce_x()

            # Collision with paddle
            if self.ball.distance(self.paddle) < 90 and self.ball.ycor() < -220:
                self.ball.bounce_y()

            # collision with brick
            for brick in self.bricks:
                if self.ball.distance(brick) < 30:
                    self.ball.bounce_y()
                    # self.ball.move_speed *= .1
                    self.increase_ball_speed(0.1)
                    self.score_board.increase_score(brick.score_value)
                    brick.hideturtle()
                    self.bricks.remove(brick)



            # Detecting Top wall collision
            if self.ball.ycor() > SCREEN_HEIGHT / 2 or self.ball.ycor() < -SCREEN_HEIGHT / 2:
                self.game_on = False
                self.game_over()

        self.screen.exitonclick()

    def outline(self):
        outline_t = Turtle()
        outline_t.color("white")
        outline_t.penup()
        outline_t.goto(-SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        outline_t.pendown()
        outline_t.pensize(3)

        for _ in range(2):
            outline_t.forward(SCREEN_WIDTH)
            outline_t.right(90)
            outline_t.forward(SCREEN_HEIGHT)
            outline_t.right(90)

    def building_bricks(self):
        bricks_x_axis = -460
        bricks_y_axis = 260
        self.bricks = []
        color_score_map = {"red": 8, "orange": 6, "yellow": 4, "green": 2}
        color = ["red", "orange", "yellow", "green"]

        for i in range(4):  # row
            for j in range(15):  # column
                brick_color = color[i]
                brick_score = color_score_map[brick_color]

                brick = Brick(position=(bricks_x_axis, bricks_y_axis), color=brick_color, score_value=brick_score)
                self.bricks.append(brick)
                bricks_x_axis += 65
            bricks_x_axis = -460
            bricks_y_axis -= 35

    def moving_paddle(self):
        if self.moving_left:
            self.paddle.move_left()
        if self.moving_right:
            self.paddle.move_right()
        self.screen.ontimer(self.moving_paddle, t=10)

    def move_left(self):
        self.moving_left = True

    def move_right(self):
        self.moving_right = True

    def stop_move(self):
        self.moving_left = False
        self.moving_right = False

    def game_over(self):
        game_over_t = Turtle()
        game_over_t.hideturtle()
        game_over_t.color("white")
        game_over_t.penup()
        game_over_t.goto(0, 0)
        game_over_t.write("GAME OVER", align="center", font=("Arial", 40, "normal"))

    def increase_ball_speed(self, increment):
        self.ball.move_speed *= (1 - increment)


BreakOut()

