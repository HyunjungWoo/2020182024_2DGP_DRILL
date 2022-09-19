import turtle


def turtle_d():
    current_x,current_y = turtle.position()
    turtle.goto(current_x+50,current_y)
    turtle.stamp()

def turtle_w():
    current_x,current_y = turtle.position()
    turtle.goto(current_x,current_y+50)
    turtle.stamp()

def turtle_a():
    current_x,current_y = turtle.position()
    turtle.goto(current_x-50,current_y)
    turtle.stamp()

def turtle_s():
    current_x,current_y = turtle.position()
    turtle.goto(current_x,current_y-50)
    turtle.stamp()

def restart():
    turtle.reset()
    
turtle.shape('turtle')

turtle.onkey(turtle_d,'d')
turtle.onkey(turtle_a,'a')
turtle.onkey(turtle_w,'w')
turtle.onkey(turtle_s,'s')
turtle.onkey(restart,'Escape')
turtle.listen()

