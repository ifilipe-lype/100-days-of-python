from turtle import Turtle


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180


class Snake:
    def __init__(self):
        """Creates a new turtle shape (snake) and print it to the screen"""
        self.segments = []
        self.create_snake()
        self.head_segment: Turtle = self.segments[0]

    def create_snake(self):
        """Creates the initial snake's body"""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)

        self.segments.append(new_segment)

    def grow(self):
        tail_segment: Turtle = self.segments[-1]

        self.add_segment(tail_segment.position())
        pass

    def move(self):
        """Moves the snake's head forward and makes the body follow (l_o_l)"""
        head_segment = self.segments[0]

        for seg_idx in range(len(self.segments) - 1, 0, -1):
            segment = self.segments[seg_idx]
            next_segment = self.segments[seg_idx - 1]

            segment.goto(next_segment.position())

        head_segment.forward(MOVE_DISTANCE)

    def up(self):
        if self.head_segment.heading() != DOWN:
            self.head_segment.setheading(UP)

    def right(self):
        if self.head_segment.heading() != LEFT:
            self.head_segment.setheading(RIGHT)

    def down(self):
        if self.head_segment.heading() != UP:
            self.head_segment.setheading(DOWN)

    def left(self):
        if self.head_segment.heading() != RIGHT:
            self.head_segment.setheading(LEFT)

    def reset(self):
        for segment in self.segments:
            segment.goto(10000, 10000)
        self.segments.clear()
        self.create_snake()
        self.head_segment: Turtle = self.segments[0]