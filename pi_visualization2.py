import turtle
import time

# windown = turtle.Screen()
# windown.screensize(7000, 5000)
turtle.setup(1.0, 1.0)
t = turtle.Turtle()
t.hideturtle()
t.pensize(8)
t.penup()
t.goto(-1000, 0)
t.pendown()
t.speed(0)
file = open('圆周率前100万位.txt')
color = ['gold', 'goldenrod', 'red', 'firebrick', 'mediumvioletred', 'darkorchid', 'royalblue', 'lightseagreen',
         'mediumseagreen', 'olivedrab']
color_fill = ['khaki', 'moccasin', 'lightcoral', 'lightsalmon', 'orchid', 'mediumpurple', 'skyblue', 'aquamarine',
              'lightgreen', 'palegreen']


def draw_dot(n: int, c: int):
    t.color(color_fill[n])
    t.begin_fill()
    t.circle(60)
    t.end_fill()
    t.color(color[n])
    t.circle(60)
    pos = t.pos()
    t.penup()
    t.goto(pos[0], pos[1] + 10)
    t.pendown()
    t.color("black")
    t.write(n, align="center", font=("Arial", 64, "bold"))

    t.penup()
    if c % 50 == 0:
        t.goto(-1500, pos[1] - 200)
    else:
        t.goto(pos[0] + 200, pos[1])
    t.pendown()


count = 1
num = 3
draw_dot(num, count)

for i in range(28):
    word = file.readline().strip()
    for a in word:
        num = int(a)
        count += 1
        if count > 1400:
            break
        draw_dot(num, count)

t.hideturtle()

# screen = turtle.Screen()
# screen.setup(7000, 5000)
# screen.tracer(False)
# screen.tracer(True)
# canvas = screen.getcanvas()
# canvas.postscript(file='pic.eps', width=7000, height=5000)
time.sleep(60)
file.close()
