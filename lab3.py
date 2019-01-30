# Lab No. 3
# CTEC 121
# Richard Mora

from graphics import * 

def snowman():
    # create the graphics window
    win = GraphWin('Lab 3 - Snowman',800,800)
    
    # your code to draw the snowman goes here
    # draw three circles for the body
    # name the three circles circle1, circle2 and circl3
    circle1 = Circle(Point(400,650),100)
    circle1.draw(win)
    circle2 = Circle(Point(400,470),80)
    circle2.draw(win)
    circle3 = Circle(Point(400,330),60)
    circle3.draw(win)



    # draw two eyes on the top circle
    # name the two eyes using variables eye1 and eye2
    eye1 = Circle(Point(380,320),10)
    eye1.draw(win)
    eye2 = eye1.clone()
    eye2.move(40,0)
    eye2.draw(win)



    # draw a nose using the polygon method and make it orange
    # name the nose using the variable nose
    # point1 = Point(390,310), Point(395,315)
    # point2 = Point(395,315), Point(385,300)
    # point3 = Point(385,300), Point(390,310)
    nose = Polygon(Point(420,340),Point(400,350),Point(400,320))
    nose.setFill("orange")
    nose.draw(win)



    # draw a hat using a rectangle and fill it with black
    # name the hat using the variable hat
    hat = Rectangle(Point(435,270), Point(365,220))
    hat.setFill("black")
    hat.draw(win)



    # draw a line to represent the rim of the hat using a line
    # name the line using the variable hatline
    hatline = Line(Point(330,270), Point(470,270))
    hatline.setWidth(2)
    hatline.draw(win)




    # close the program
    input('Press enter to quit the program ')
    # close the graphics window
    win.close()


# Call the snowman() function to start the program
snowman()