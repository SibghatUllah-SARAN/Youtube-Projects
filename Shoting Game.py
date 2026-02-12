import turtle
import time

# Screen
wn = turtle.Screen()
wn.title("🔫 Shooting Game | CodeNovaX")
wn.bgcolor("#020617")
wn.setup(900, 650)
wn.tracer(0)

# Player
player = turtle.Turtle()
player.shape("triangle")
player.color("#22c55e")
player.penup()
player.goto(0, -250)

# Bullet
bullet = turtle.Turtle()
bullet.shape("circle")
bullet.color("#ef4444")
bullet.penup()
bullet.goto(0, -200)
bullet.hideturtle()
bullet.state = "ready"

# Enemy
enemy = turtle.Turtle()
enemy.shape("square")
enemy.color("#f97316")
enemy.penup()
enemy.goto(0, 200)

enemy_speed = 3

# Move Player
def move_left():
    x = player.xcor() - 25
    if x > -420:
        player.setx(x)

def move_right():
    x = player.xcor() + 25
    if x < 420:
        player.setx(x)

# Fire Bullet
def fire_bullet():
    global bullet
    if bullet.state == "ready":
        bullet.state = "fire"
        bullet.goto(player.xcor(), player.ycor()+20)
        bullet.showturtle()

# Keyboard
wn.listen()
wn.onkeypress(move_left, "a")
wn.onkeypress(move_right, "d")
wn.onkeypress(fire_bullet, "space")

# Main Loop
while True:
    wn.update()

    # Enemy movement
    x = enemy.xcor()
    x += enemy_speed
    enemy.setx(x)

    if enemy.xcor() > 420 or enemy.xcor() < -420:
        enemy_speed *= -1
        enemy.sety(enemy.ycor() - 40)

    # Bullet movement
    if bullet.state == "fire":
        bullet.sety(bullet.ycor() + 10)

    # Bullet off screen
    if bullet.ycor() > 300:
        bullet.hideturtle()
        bullet.state = "ready"

    # Collision
    if bullet.distance(enemy) < 25:
        enemy.goto(0, 200)
        bullet.hideturtle()
        bullet.state = "ready"
