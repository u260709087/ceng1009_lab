# def gradeMark(mark):
#     if mark >= 90:
#         return "A"
#     elif mark >= 80:
#         return "B"
#     elif mark >= 70:
#         return "C"
#     elif mark >= 60:
#         return "D"
#     else:
#         return "F"
#
# marks = [95, 90, 89.9, 88, 79.9, 70, 65, 60, 59.5, 0]
# for mark in marks:
#     print("Grade is ", gradeMark(mark))
#
# mark= float(input("Enter mark: "))
# print("Grade is ", gradeMark(mark))

# import turtle
#
# def chooseColor(height):
#     if height >= 200:
#         return "red"
#     elif height >= 100:
#         return "yellow"
#     else:
#         return "green"
#
# def drawBar(t, height,gap):
#      t.penup()
#      t.left(90)
#      if height >= 0:
#        t.forward(height+gap)
#        t.write(" "+str(height))
#        t.backward(height+gap)
#      else:
#        t.fd(gap)
#        t.write(" "+str(height))
#        t.bk(gap)
#
#      t.right(90)
#      t.pendown()
#
#
#
#      t.fillcolor(chooseColor(height))
#      t.begin_fill()
#      t.left(90)
#      t.forward(height)
#      t.right(90)
#      t.forward(40)
#      t.right(90)
#      t.forward(height)
#      t.left(90)
#      t.end_fill()
#
# def barChart(data):
#          maxheight = max(data)
#
#          num_bars = len(data)
#          border = 10
#
#          gap = (maxheight - border) / 25
#
#          wn = turtle.Screen()
#          wn.bgcolor("lightgreen")
#
#          right = 40 * num_bars + border
#          top = maxheight + 4 * border
#
#          wn.setworldcoordinates(-border, -border, right, top)
#          t = turtle.Turtle()
#          t.color("blue")
#          t.fillcolor("red")
#          t.pensize(3)
#          for height in data:
#              drawBar(t, height, gap)
#
#          wn.exitonclick()
#
# data = [-48, 117, 200, 240, 160, 260, -220]
# barChart(data)


def findHypot(side1, side2):
    return (side1**2 + side2**2)**0.5
side1= float(input("Enter the length of side 1: "))
side2= float(input("Enter the length of side 2: "))
print(findHypot(side1, side2))