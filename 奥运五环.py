import turtle    #导入海龟函数
turtle.width(10)  #设置画笔宽度
turtle.color("blue") #设置画笔颜色
turtle.circle(50)   #设置圆半径

turtle.penup()   # 抬笔
turtle.goto(120,0)
turtle.color("black")
turtle.pendown() #落笔
turtle.circle(50)


turtle.penup()
turtle.goto(240,0)
turtle.color("red")
turtle.pendown()
turtle.circle(50)


turtle.penup()
turtle.goto(60,-50)
turtle.color("yellow")
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(180,-50)
turtle.color("green")
turtle.pendown()
turtle.circle(50)
