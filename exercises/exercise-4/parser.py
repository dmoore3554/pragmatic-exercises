from turtle import *
import time
t = Turtle()

def select_pen(number):
    t.pensize(number)

def pen_down():
    t.down()

def pen_up():
    t.up()

def draw_north(distance):
    t.setheading(90)
    t.forward(distance * 100)

def draw_east(distance):
    t.setheading(0)
    t.forward(distance * 100)

def draw_south(distance):
    t.setheading(270)
    t.forward(distance * 100)

def draw_west(distance):
    t.setheading(180)
    t.forward(distance * 100)

commands = {
    "P" : select_pen,
    "D" : pen_down,
    "U" : pen_up,
    "N" : draw_north,
    "E" : draw_east,
    "S" : draw_south,
    "W" : draw_west
}

with open("exercises/exercise-4/turtle-code.txt", "r") as file:
    for line in file:
        time.sleep(1)
        command = line.split()
        function = commands.get(command[0])
        if len(command) > 1:
            function(int(command[1]))
        else:
            function()