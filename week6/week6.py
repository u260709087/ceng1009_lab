import turtle

# -- setup --

wn = turtle.Screen()
wn.bgcolor("lightgreen")

t = turtle.Turtle()

# -- functions --

def drawPoly(someturtle, somesides, somesize):
    angle = 360 / somesides
    for i in range(somesides):
        someturtle.fd(somesize)
        someturtle.left(angle)

def drawSpiral(someturtle, angle):
    size = 1
    for i in range(100):
        someturtle.fd(size)
        someturtle.right(angle)
        size = size+2

def drawEquitriangle(someturtle, somesize):
    drawPoly(someturtle, 3, somesize)

def drawStar(someturtle, size):
    for i in range(5):
        someturtle.fd(size)
        someturtle.right(144)

def drawSprite(someturtle, legs, length):
    angle = 360 / legs
    t.shape("circle")
    t.stamp()
    for i in range(legs):
        someturtle.fd(length)
        someturtle.bk(length)
        someturtle.left(angle)




# -- exercises --
# Exercise 1
# t.pencolor("hotpink")
# drawPoly(t, 8, 50)


# Exercise 2
# t.pencolor("blue")
# for i in range(20):
#     drawPoly(t, 4, 50)
#     t.left(162)
#


# Exercise 3
# t.pencolor("blue")
# t.penup()
# t.goto(-200,0)
# t.pendown()
# drawSpiral(t, 90)
#
# t.penup()
# t.goto(0,0)
# t.pendown()
#
# drawSpiral(t, 89)


# Exercise 4
# drawEquitriangle(t, 100)


# Exercise 5
# t.color("hotpink")
# for i in range(5):
#     drawStar(t, 50)
#     t.penup()
#     t.fd(200)
#     t.right(144)
#     t.pendown()

# Exercise 6
# drawSprite(t, 15, 120)




# -- finish --
wn.exitonclick()



