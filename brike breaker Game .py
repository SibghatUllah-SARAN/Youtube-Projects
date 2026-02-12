import turtle

# Screen
wn = turtle.Screen()
wn.title("🧱 Brick Breaker | CodeNovaX")
wn.bgcolor("#020617")
wn.setup(900, 650)
wn.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("#38bdf8")
paddle.shapesize(stretch_wid=1, stretch_len=6)
paddle.penup()
paddle.goto(0, -270)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("#22c55e")
ball.penup()
ball.goto(0, -200)
ball.dx = 0.25
ball.dy = 0.25

# Bricks
bricks = []
colors = ["#ef4444", "#f97316", "#eab308", "#22c55e"]

for y in range(200, 100, -40):
    for x in range(-400, 401, 80):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colors[(x+y) % 4])
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        brick.goto(x, y)
        bricks.append(brick)

# Paddle movement
def move_left():
    paddle.setx(paddle.xcor() - 30)

def move_right():
    paddle.setx(paddle.xcor() + 30)

wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

# Game loop
while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.xcor() > 430 or ball.xcor() < -430:
        ball.dx *= -1

    if ball.ycor() > 300:
        ball.dy *= -1

    if ball.ycor() < -300:
        ball.goto(0, -200)

    # Paddle collision
    if (paddle.ycor() < ball.ycor() < paddle.ycor() + 20) and \
       (paddle.xcor()-70 < ball.xcor() < paddle.xcor()+70):
        ball.dy *= -1

    # Brick collision
    for brick in bricks:
        if ball.distance(brick) < 35:
            brick.goto(1000, 1000)
            bricks.remove(brick)
            ball.dy *= -1
