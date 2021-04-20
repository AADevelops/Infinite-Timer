hours = 0 
minutes = 0
seconds = 0

import time
import turtle

tl = turtle.Turtle()
screen = turtle.Screen()
screen.title("Infinite Timer")

while True:
    tl.hideturtle()
    tl.clear()
    tl.write(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2), font = ("Arial", 40), align = "center")
    seconds += 1
    time.sleep(1)
    if seconds == 60:
        seconds = 0 
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1
