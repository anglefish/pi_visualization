import turtle
import time

# windown = turtle.Screen()
# windown.screensize(7000, 5000)
turtle.setup(1.0, 1.0)
t = turtle.Turtle()
t.hideturtle()
t.pensize(4)
t.penup()
t.goto(0, -500)
t.pendown()
t.left(90)
t.speed(0)
file = open('圆周率前100万位.txt')
color = ['gold', 'goldenrod', 'red', 'firebrick', 'mediumvioletred', 'darkorchid', 'royalblue', 'lightseagreen',
         'mediumseagreen', 'greenyellow']
last_num = 3
t.color(color[last_num])
t.right(last_num * 36)
t.forward(40)
for i in range(100):
    word = file.readline().strip()
    for a in word:
        current_num = int(a)
        t.color(color[current_num])
        angle = (current_num - last_num) * 36
        t.right(angle)
        t.forward(40)
        last_num = current_num
t.hideturtle()

# screen = turtle.Screen()
# screen.setup(7000, 5000)
# screen.tracer(False)
# screen.tracer(True)
# canvas = screen.getcanvas()
# canvas.postscript(file='pic.eps', width=7000, height=5000)
time.sleep(10)
file.close()
