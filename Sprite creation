import turtle

wn = turtle.Screen()
sprite = turtle.Turtle()
legs = int(input("Enter the number of legs for the sprite:"))
angle = 360 / legs
sprite.color("blue")

# To draw the legs
for i in range(legs):           
    sprite.right(angle)
    sprite.forward(50)
    sprite.stamp()
    sprite.speed = 20
    sprite.shape("star")
#The below 3 lines are to go from the middle to the different directions
    sprite.right(180)
    sprite.forward(50)
    sprite.right(180)

wn.exitonclick()
