import turtle

BODY_COLOR ='red'
GLASS_COLOR = 'skyblue'

t=turtle.Turtle()


def body():
    t.pensize(20)
    #t.speed(15)

    t.fillcolor(BODY_COLOR)
    t.begin_fill()

    #right side
    t.right(90)
    t.forward(50)
    t.right(180)
    t.circle(40,-180)
    t.right(180)
    t.forward(200)

    #head curve
    t.right(180)
    t.circle(180,-180)

    #left side
    t.backward(20)
    t.left(15)
    t.circle(500,20)
    t.backward(20)

    #t.backward(200)
    t.circle(40,-180)
    #t.right(90)
    t.left(7)
    t.backward(50)

    #hip
    t.up()
    t.left(90)
    
