import turtle

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")


for i in range(100):

    my_turtle.forward(100 + i)
    my_turtle.right(60)

turtle.done()