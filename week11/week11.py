# def fizz_buzz(n):
#
#     for i in range(n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)
# fizz_buzz(10)


# def digit_sum(n):
#     total = 0
#     while n > 0:
#         total += n % 10
#         n = n//10
#     return total
# print(digit_sum(1234))


# def alternate_case(s):
#     str = ""
#     for i in range(len(s)):
#         if i % 2 == 0:
#             str = str + s[i].upper()
#         else:
#             str = str + s[i].lower()
#     return str
# print(alternate_case("hello world"))

# import turtle
# t=turtle.Turtle()
# wn=turtle.Screen()
# def draw_polygon(t,sides,length):
#     for i in range(sides):
#         t.fd(length)
#         t.lt(360/sides)
#
# wn.bgcolor("lightgreen")
# t.pensize(3)
# colors = ["red", "yellow", "blue"]
#
# for i in range(3):
#     t.penup()
#     t.goto(-150 + i*120, -30)
#     t.pendown()
#     t.color(colors[i])
#     draw_polygon(t, i+3, 60)
# wn.exitonclick()

# import turtle
#
# def filled_square(t, size, color):
#     t.fillcolor(color)
#     t.begin_fill()
#
#     for i in range(4):
#         t.fd(size)
#         t.lt(90)
#
#     t.end_fill()
#
# t = turtle.Turtle()
# wn = turtle.Screen()
# colors = ["red", "blue", "red", "blue", "red"]
#
# for i in range(5):
#     t.penup()
#     t.goto(-165 + i*70, -25)
#     t.pendown()
#     filled_square(t, 50, colors[i])

# import turtle
# def drawSquare(t,sides,length):
#     for i in range(sides):
#         t.fd(length)
#         t.lt(90)
#
# t = turtle.Turtle()
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# t.pensize(2)
#
# for i in range(12):
#     drawSquare(t, 4, 80)
#     t.lt(30)
# wn.exitonclick()


# import turtle
# t = turtle.Turtle()
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
#
# def drawSquare(t, size, filled):
#     if filled:
#         t.begin_fill()
#     for i in range(4):
#         t.fd(size)
#         t.left(90)
#     if filled:
#         t.end_fill()
#
# size = 40
# for row in range(6):
#     for col in range(6):
#         t.penup()
#         t.goto(-120 + col * size, -120 + row * size)
#         t.pendown()
#         drawSquare(t, size, (row + col)%2==0)
# wn.exitonclick()