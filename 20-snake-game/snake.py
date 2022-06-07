from turtle import Turtle


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        """Creates a new turtle shape (snake) and print it to the screen"""
        self.segments = []
        self.create_snake()

    def create_snake(self):
        """Creates the initial snake's body"""
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)

            self.segments.append(new_segment)

    def move(self):
        """Moves the snake's head forward and makes the body follow (l_o_l)"""
        head_segment = self.segments[0]

        for seg_idx in range(len(self.segments) - 1, 0, -1):
            segment = self.segments[seg_idx]
            next_segment = self.segments[seg_idx - 1]

            segment.goto(next_segment.position())

        head_segment.forward(20)