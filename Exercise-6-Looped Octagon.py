import turtle
wn = turtle.Screen()
wn.bgcolor("yellow")
wn.title("Exercise 6 Triangle Loop")

richie = turtle.Turtle()
richie.color("blue")
richie.pensize(7) 

for f in [richie.forward(40), richie.left(45), richie.forward(40), richie.left(45), richie.forward(40), richie.left(45),richie.forward(40), richie.left(45), richie.forward(40), richie.left(45), richie.forward(40),richie.left(45), richie.forward(40),richie.left(45), richie.forward(40),richie.left(45)]:
    octagon = richie
    print(octagon) 


wn.mainloop