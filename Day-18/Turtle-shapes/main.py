
# from turtle import Turtle, Screen
# #
# # tim = Turtle()
# # tim.shape("turtle")
# # tim.color("red")
# # tim.forward(150)
# # tim.right(90)
# # tim.forward(150)
# # tim.right(90)
# # tim.forward(150)
# # tim.right(90)
# # tim.forward(150)
#
# # import turtle as t #Aliases
# # tim = t.Turtle()
# #
# # import heroes
# # print(heroes.gen())
# #
# # import turtle as t
# # tim = t.Turtle()
# #
# #
# # for _ in range(15):
# #
# #     tim.forward(10)
# #     tim.penup()
# #     tim.forward(10)
# #     tim.pendown()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # screen = Screen()
# # screen.exitonclick()
#
#
import turtle as t


tim = t.Turtle()
colours = ["dark","slate blue","violet red","lime","deep pink","black,cyan"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.left(angle)


for shape_side_n in range(3,11):
    draw_shape(shape_side_n)
##random colore and directions
#
# import turtle as t
# import random
#
# tim =t.Turtle()
# t.colormode(255)
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0, 255)
#     color = (r,g,b)
#     return color
#
#
# tim.speed("fastest")
# def draw_spirograph(size_of_gap):
#
#     for _ in range(int(360/ size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
# draw_spirograph(5)
#
# screen = t.Screen()
# screen.exitonclick()
#
# random_color()
#