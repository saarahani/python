#old snake game
import turtle
import time
import random

delay = 0.1


score = 0
high_score = 0


ts  = turtle.Screen()
ts.title("Snake Game")
ts.bgcolor("black")
ts.setup(width=610, height=610)
ts.tracer(0)


head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"


food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("pink")
food.penup()
food.goto(0, 100)

segments = []


title = turtle.Turtle()
title.speed(0)
title.shape("square")
title.color("white")
title.penup()
title.hideturtle()
title.goto(0, 260)
title.write("Score: 0  High Score: 0", align="center", font=("Courier", 22, "normal"))
title.color("pink")
title.goto(0, 220)
title.write("use (wasd)", align="center", font=("Courier", 22, "normal"))


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)



ts.listen()
ts.onkeypress(go_up, "w")
ts.onkeypress(go_down, "s")
ts.onkeypress(go_left, "a")
ts.onkeypress(go_right, "d")

while True:
    ts.update()


    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"


        for segment in segments:
            segment.goto(1000, 1000)


        segments.clear()


        score = 0


        delay = 0.1

        title.clear()
        title.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    if head.distance(food) < 20:

        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)


        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)


        delay -= 0.001


        score += 10

        if score > high_score:
            high_score = score

        title.clear()
        title.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)


    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()


    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"


            for segment in segments:
                segment.goto(1000, 1000)


            segments.clear()


            score = 0


            delay = 0.1


            title.clear()
            title.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Comic Sans", 24, "normal"))

    time.sleep(delay)

wn.mainloop()