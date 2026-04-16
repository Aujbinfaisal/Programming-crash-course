# Final Project
# CS 111, Hayes & Reckinger
# Auj bin Faisal
# Python Basics

import turtle
import random

# go to the previous screen
def back_button(screen_name):

    back.up()
    back.goto(-675,320)
    back.down()
    back.color('gold1')
    back.write('<<< Back', True, align = 'left', font = ('times new roman', 20, 'bold'))

    screen_name.onclick(back_button2)

def back_button2(x, y):

    if back.distance(x, y) <= 75:
        branching.clear()
        loops.clear()
        io.clear()
        turtles.clear()
        for_.clear()
        while_.clear()
        t.clear()
        t2.clear()
        bulb.hideturtle()
        icon.hideturtle()
        oven.hideturtle()
        cake.hideturtle()
        car.hideturtle()

        screen2()
        back.clear()

# makes a rounded quadilateral with text
def draw_box(color, height, width, t1, loc, text, text_color, font):
    turtle.tracer(0)
    turtle.hideturtle()

    t1.hideturtle()
    t1.up()
    t1.goto(loc)
    t1.down()
    t1.color(color)


    t1.begin_fill()
    for i in range(2):
        t1.fd(width)
        t1.circle(20, 90)
        t1.fd(height)
        t1.circle(20, 90)
    t1.end_fill()
    t1.up()

    x, y = t1.pos()
    t1.goto(x + width/2, y + height/1.7)
    t1.color(text_color)
    t1.write(text, True, align = 'center', font = ('times new roman', font, 'bold'))
    t1.color(color)

# welcome screen
def screen2():
    t.clear()
    s2 = turtle.getscreen()
    s2.bgpic(images[1])

    t.color('white')
    t.goto(0, 314)
    text = 'Welcome to your Python Basics Class ' + name + '! What would you like to learn first?'
    t.write(text, False, align = 'center', font = ('times new roman', 26 , 'normal'))

    draw_box('medium purple', 100, 100, branching, (-500, 150), 'Branching', 'pale turquoise', 12)
    draw_box('medium purple', 100, 100, loops, (-500, -275), 'Loops', 'pale turquoise', 12)
    draw_box('medium purple', 100, 100, io, (400, 150), 'Input/Output', 'pale turquoise', 12)
    draw_box('medium purple', 100, 100, turtles, (400, -275), 'Turtles', 'pale turquoise', 12)

    s.onclick(next_screen)

# check where the user clicked and decides which screen to go to next
def next_screen(x, y):
    branching.clear()
    loops.clear()
    io.clear()
    turtles.clear()
    if branching.distance(x, y) <= 300:
        branch_screen()
    elif loops.distance(x, y) <= 300:
        loops_screen()
    elif io.distance(x, y) <= 300:
        io_screen()
    elif turtles.distance(x, y) <= 300:
        turtles_screen()
    

# new screen for branching
def branch_screen():
    s.tracer(True)
    t.clear()
    s_branch = turtle.getscreen()
    s_branch.bgpic('nopic')
    s_branch.bgcolor('teal')
    back_button(s_branch) 

    branching.color('darkgreen')
    branching.goto(0, 300)
    branching.write('Branching', False, align = 'center', font = ('Arial', 33 , 'underline'))

    branching.color('green1')
    x = -600
    y = 200
    branching.goto(x, y)

    line1 = '- Branching usually contains a true or false statement, and 2 different outcomes depending on the branch.'
    branching.write(line1, False, font = ('Arial', 18 , 'normal'))
    
    branching.goto(x, y - 50)
    line2 = '- For example, IF night-time, turn light on, ELSE keep light off'
    branching.write(line2, False, font = ('Arial', 18 , 'normal'))

    branching.goto(x, y - 100)
    line3 = '- Press "r" to repeat, or click back to learn something new!'
    branching.write(line3, False, font = ('Arial', 18 , 'normal'))

    time = ['sun.gif', 'moon.gif']
    bulbs = ['light_off.gif', 'light_on.gif']
    index = random.randint(0,1)
    
    bulb.up()
    icon.up()

    turtle.addshape('sun.gif')
    turtle.addshape('moon.gif')
    turtle.addshape('light_off.gif')
    turtle.addshape('light_on.gif')  
    
    bulb.shape(bulbs[index])
    icon.shape(time[index])

    bulb.goto(222, -100)
    bulb.showturtle()

    icon.goto(-222, -100)
    icon.showturtle()    

    turtle.onkey(branch_screen, 'r')
    turtle.listen()


# new screen for loops
def loops_screen():
    t.clear()
    s_loop = turtle.getscreen()
    s_loop.bgpic(images[2])
    turtle.bgcolor('gray16')

    draw_box('light gray', 400, 200, for_, (-500, -200), '  For\nLoops', 'turquoise4', 15)
    draw_box('light gray', 400, 200, while_, (300, -200), 'While \nLoops', 'turquoise4', 15)

    s_loop.onclick(next_screen2)

# new screen for fucntions
def io_screen():
    s.tracer(True)
    t.clear()
    s_io = turtle.getscreen()
    s_io.bgpic('nopic')
    s_io.bgcolor('sea green')
    back_button(s_io)

    io.color('darkslategray1')
    io.goto(0, 300)
    io.write('Input/Output', False, align = 'center', font = ('Arial', 33 , 'underline'))

    io.color('dark slate gray')
    x = -600
    y = 200
    io.goto(x, y)

    line1 = '- One of the core concepts of programming is input, processing, and output'
    io.write(line1, False, font = ('Arial', 18 , 'normal'))
    
    io.goto(x, y - 50)
    line2 = '- For example, a user may input from a touchscreen, where the microprocessor does the processing, and finally'
    io.write(line2, False, font = ('Arial', 18 , 'normal'))

    io.goto(x + 15, y - 100)
    line3 = 'the screen outputs the final product.'
    io.write(line3, False, font = ('Arial', 18 , 'normal'))

    turtle.addshape('ingredients.gif')
    turtle.addshape('oven.gif')
    turtle.addshape('cake.gif')

    oven.shape('oven.gif')
    oven.up()
    oven.goto(0, -100)
    oven.showturtle()

    ingredients.shape('ingredients.gif')
    ingredients.up()
    ingredients.goto(-400, -100)
    ingredients.showturtle()
    for i in range(400):
        ingredients.fd(1)
    ingredients.hideturtle()

    cake.shape('cake.gif')
    cake.up()
    cake.goto(0, -100)
    cake.showturtle()
    for j in range(300):
        cake.fd(1)


# new screen for turtles
def turtles_screen():
    s.tracer(True)
    t.clear()
    s_turtles = turtle.getscreen()
    s_turtles.bgpic('nopic')
    s_turtles.bgcolor('hotpink4')
    back_button(s_turtles)

    turtles.color('hotpink1')
    turtles.goto(0, 300)
    turtles.write('Turtle Graphics', False, align = 'center', font = ('Arial', 33 , 'underline'))

    turtles.color('pink')
    x = -600
    y = 200
    turtles.goto(x, y)

    line1 = '- Turtle graphics can help visualse your code'
    turtles.write(line1, False, font = ('Arial', 18 , 'normal'))
    
    turtles.goto(x, y - 50)
    line2 = '- This very application was made using turtle graphics!'
    turtles.write(line2, False, font = ('Arial', 18 , 'normal'))

    turtles.goto(x, y - 100)
    line3 = '- Here are some basic turtle functions:'
    turtles.write(line3, False, font = ('Arial', 18 , 'normal'))


    
    t.color('black')
    t.shape('turtle')
    t.speed(1)
    turtles.color('white')
    
    t.goto(-300, 0)
    t.showturtle()

    turtles.goto(-350, 0)
    turtles.write('pendown()', False, font = ('Arial', 16 , 'normal'))
    turtles.goto(-350, -25)
    turtles.write('forward(500)', False, font = ('Arial', 16 , 'normal'))

    t.down()
    t.fd(500)
    t.right(90)
    
    turtles.goto(210, 0)
    turtles.write('right(90)', False, font = ('Arial', 16 , 'normal'))
    turtles.goto(210, -25)
    turtles.write('backward(300)', False, font = ('Arial', 16 , 'normal'))

    t.bk(300)

    turtles.goto(200, 300)
    turtles.write('forward(500)', False, font = ('Arial', 16 , 'normal'))

    t.fd(500)

    turtles.goto(210, -220)
    turtles.write('left(180)', False, font = ('Arial', 16 , 'normal'))
    turtles.goto(210, -245)
    turtles.write('circle(200, 180)', False, font = ('Arial', 16 , 'normal'))

    t.left(180)
    t.circle(200, 180)

    turtles.goto(-370, -220)
    turtles.write('color("light gray")', False, font = ('Arial', 16 , 'normal'))
    turtles.goto(-560, -245)
    turtles.write('repeat circle(n/2 , 180) 7 times to make spiral', False, font = ('Arial', 16 , 'normal'))

    t.color('light gray')
    t.circle(100, 180)
    t.circle(50, 180)
    t.circle(25, 180)
    t.circle(12, 180)
    t.circle(6, 180)
    t.circle(3, 180)
    t.circle(1, 180)

    turtles.goto(-305, -270)
    turtles.write('hideturtle()', False, font = ('Arial', 16 , 'normal'))

    t.up()
    t.hideturtle()


# check which loop screen the user selected
def next_screen2(x, y):
    turtle.addshape('car.gif')
    s.tracer(True)

    for_.clear()
    while_.clear()
    if for_.distance(x, y) <= 350:
        for_screen()
    elif while_.distance(x, y) <= 350:
        while_screen()

def for_screen():
    s_for = turtle.getscreen()
    s_for.bgpic('nopic')
    s_for.bgcolor('wheat')
    back_button(s_for)

    for_.color('orange')
    for_.goto(0, 300)
    for_.write('For Loops', False, align = 'center', font = ('Arial', 33 , 'underline'))

    for_.color('orange3')
    x = -600
    y = 200
    for_.goto(x, y)

    line1 = '- For loops repeat a specified chunk of code for a set amount of times'
    for_.write(line1, False, font = ('Arial', 18 , 'normal'))

    car.shape('car.gif')
    car.up()
    car.goto(-500, -100)
    car.showturtle()

    index = turtle.textinput('Iterations', "How many times shoud the car loop?")

    for i in range(int(index)):
        for i in range(2):
            car.fd(800)
            car.left(90)
            car.fd(250)
            car.left(90)
        

def while_screen():
    s.tracer(False)
    s_while = turtle.getscreen()
    s_while.bgpic('nopic')
    s_while.bgcolor('light sea green')
    back_button(s_while)

    car.shape('car.gif')
    car.up()
    car.goto(-500, -100)
    car.showturtle()

    turtles.color('blue')
    turtles.goto(0, 300)
    turtles.write('While loops', False, align = 'center', font = ('Arial', 33 , 'underline'))

    turtles.color('deep sky blue')
    x = -600
    y = 200
    turtles.goto(x, y)

    line1 = '- While loops also repeat a specified chunk of code, until a condition is satisfied/broken'
    turtles.write(line1, False, font = ('Arial', 18 , 'normal'))

    turtles.goto(x, y - 50)
    line2 = '- WHILE the light is green, the car can move.'
    turtles.write(line2, False, font = ('Arial', 18 , 'normal'))

    car.speed(1)
    t.up()
    t2.up()
    t.speed(10)
    t2.speed(10)

    while car.distance(t2) >= 300:
        i = random.randint(0,1)
        
        if i == 1:
            t.clear()
            t2.clear()

            t2.goto(550, 150)
            t2.color('green')
            t2.down()
            t2.begin_fill()
            t2.circle(50, 360)
            t2.end_fill()
            t2.up()

            s_while.tracer(True)
            car.fd(100)

        elif i == 0:
            t.clear()
            t2.clear()

            t.goto(400, 150)
            t.color('red')
            t.down()
            t.begin_fill()
            t.circle(50, 360)
            t.end_fill()
            t.up()
    
    t.clear()
    t2.clear()



if __name__ == '__main__':
    global images
    global name

    file_ = open('images.txt')
    Images = file_.readlines()
    images = []

    for image in range(len(Images)):
        img2 = Images[image].lower().strip()
        images.append(img2)        

    # Making a screen object
    s = turtle.getscreen()
    s.bgpic(images[0])

    # Making a turtle object
    turtle.hideturtle()
    turtle.speed(1)
    t = turtle.Turtle() 
    t.hideturtle()
    t.up()
    t.color('blue')
    t.goto(0, 200)
    t.write('Press enter to start!', False, align = 'center', font = ('times new roman', 50 , 'normal'))

    name = turtle.textinput('Name', "What's your name?")

    branching = turtle.Turtle()
    loops = turtle.Turtle()
    io = turtle.Turtle()
    turtles = turtle.Turtle()
    for_ = turtle.Turtle()
    while_ = turtle.Turtle()
    back = turtle.Turtle()
    bulb = turtle.Turtle()
    icon = turtle.Turtle()
    ingredients = turtle.Turtle()
    oven = turtle.Turtle()
    cake = turtle.Turtle()
    car = turtle.Turtle()
    t2 = turtle.Turtle()

    branching.hideturtle()
    loops.hideturtle()
    io.hideturtle()
    turtles.hideturtle()
    for_.hideturtle()
    while_.hideturtle()
    back.hideturtle()  
    bulb.hideturtle()
    icon.hideturtle()
    ingredients.hideturtle()
    oven.hideturtle()
    cake.hideturtle()  
    car.hideturtle()
    t2.hideturtle()


    turtle.onkey(screen2, 'Return')

    turtle.listen()
    turtle.mainloop()