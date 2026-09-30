
from turtle import*

width(7)
shape("turtle")
begin_fill()
color("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
forward(70)

begin_fill()
color("pink")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()
color("red")
begin_fill()

right(150)
forward(200)
left(120)
forward(200)
end_fill()
penup()
goto(0,150)

pendown()

# forward(-50)
begin_fill()
color("black")

right(60)
forward(-40)
right(90)
forward(-50)
left(90)
forward(40)
right(90)
forward(40)
end_fill()
right(60)

penup()
goto(70,100)
forward(100)
pendown()

begin_fill()
color("black")

left(60)
forward(-45)
left(90)
forward(-40)
right(90)
forward(45)
left(90)
forward(50)
end_fill()
left(60)


exitonclick()