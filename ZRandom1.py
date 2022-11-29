import turtle

squary = turtle.Turtle()
squary.speed(50000)

c = ["black", "red"]

for i in range(720): # this "for" loop will repeat these functions 500 times
    #squary.pencolor(c[i%2])
    squary.circle(((i//72) * 20) + 50)
    squary.left(20)