import turtle

window = turtle.Screen()
window.bgcolor("darkblue")
def draw_square():    
    john = turtle.Turtle()
    john.shape("turtle")
    john.color("green")
    john.speed(3)

    num=0
    while num < 4:
        john.forward(100)
        john.right(90)
        num += 1
draw_square()

def draw_circle():
    arnold = turtle.Turtle()
    arnold.shape("arrow")
    arnold.color("purple")
    arnold.circle(100)
    arnold.speed(3)    
draw_circle()

def draw_triangle():
    sally = turtle.Turtle()
    sally.shape("turtle")
    sally.color("yellow")
    sally.speed(3)

    num=0
    while num < 3:
        sally.forward(100)
        sally.right(120)
        num += 1
draw_triangle()

def draw_squarecircle():
    john = turtle.Turtle()
    john.shape("turtle")
    john.color("orange")
    john.speed(5)
    john.right(10)
    for i in range(1,36):
        num=0
        while num < 4:
            john.forward(100)
            john.right(90)
            num += 1
        john.right(10)
draw_squarecircle()

window.exitonclick()
