import turtle
import math

def game():
    # 壁にぶつかったらタートルを跳ね返す
    if math.fabs(my_turtle.xcor()) >= X_LIMIT:
        angle = 180 - my_turtle.heading()
        my_turtle.setheading(angle)
    if my_turtle.ycor() >= Y_LIMIT:
        angle = 360 - my_turtle.heading()
        my_turtle.setheading(angle)

    my_turtle.forward(step)

    # 画面をアップデート
    screen.update()
    screen.ontimer(game, 10)

def tleft():
    # 左に回転
    my_turtle.left(10)

def tright():
    # 右に回転
    my_turtle.right(10)

screen = turtle.Screen()
screen.setup(700, 700)
screen.title("ゲーム")

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.shapesize(3)
my_turtle.color("orange")
my_turtle.penup()

# トレーサーをオフ
screen.tracer(0)

# キーイベント
screen.listen()
screen.onkey(tleft, "Left")
screen.onkey(tright, "Right")

# 境界
X_LIMIT = 300
Y_LIMIT = 300

# タートルのループごとの移動距離
step = 3
# タートルの角度
angle = 40
my_turtle.left(angle)

# ゲーム開始
game()

screen.mainloop()
