from turtle import *

class parser:
    def __init__(self):
        self.t = Turtle()
        self.commands = {
            "P" : self.select_pen,
            "D" : self.pen_down,
            "U" : self.pen_up,
            "N" : self.draw_north,
            "E" : self.draw_east,
            "S" : self.draw_south,
            "W" : self.draw_west
        }

    def select_pen(self, number):
        self.t.pensize(number)

    def pen_down(self, ):
        self.t.down()

    def pen_up(self, ):
        self.t.up()

    def draw_north(self, distance):
        self.t.setheading(90)
        self.t.forward(distance * 100)

    def draw_east(self, distance):
        self.t.setheading(0)
        self.t.forward(distance * 100)

    def draw_south(self, distance):
        self.t.setheading(270)
        self.t.forward(distance * 100)

    def draw_west(self, distance):
        self.t.setheading(180)
        self.t.forward(distance * 100)

    def run_program(self, file_path):
        with open(file_path, "r") as file:
            for line in file:
                command = line.split()
                function = self.commands.get(command[0])
                if len(command) > 1:
                    function(int(command[1]))
                else:
                    function()

my_parser = parser()
my_parser.run_program("exercises/exercise-4/turtle-code.txt")