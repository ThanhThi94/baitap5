import turtle
n = turtle.Turtle()
n.pensize(5)
n.pencolor("Blue")
n.speed(200)
#khuon mat
n.penup()
n.goto(0, -200)
n.pendown()
n.circle(200)

#mat
n.penup()
n.goto(-100,50)
n.pendown()

eye_size = 17.5

n.fillcolor('red')
n.begin_fill()
n.circle(eye_size)
n.end_fill()

n.penup()
n.goto(100, 50)
n.pendown()
n.begin_fill()
n.circle(eye_size)
n.end_fill()
#mui
n.penup ()
n.goto(0,0)
n.pendown()
n.circle(-10, steps=3)
#mieng
n.fillcolor('yellow')
n.begin_fill()
n.penup()
n.goto(-100, -50)
n.pendown()
n.right(90)
n.circle(100,180)
n.left(90)
n.forward(200)
n.end_fill()



turtle.done()