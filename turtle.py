import turtle
t = turtle.Turtle()
t.shape("turtle")

color = [0] * 3
color[0] = input("색상 #1을 입력하시오: ")
color[1] = input("색상 #2을 입력하시오: ")
color[2] = input("색상 #3을 입력하시오: ")
 
t.fillcolor(color[0])
t.begin_fill()
t.circle(50)
t.end_fill()
 
t.up()
t.fd(100)
t.down()
 
t.fillcolor(color[1])
t.begin_fill()
t.circle(50)
t.end_fill()
 
t.up()
t.fd(100)
t.down()
 
t.fillcolor(color[2])
t.begin_fill()
t.circle(50)
t.end_fill()
