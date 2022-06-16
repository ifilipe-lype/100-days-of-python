import turtle
import pandas as pd

US_IMG_PATH = "blank_states_img.gif"

screen = turtle.Screen()

# screen setup
screen.title("U.S. States Game")
screen.addshape(US_IMG_PATH)

turtle.shape(US_IMG_PATH)

state_cors_data = pd.read_csv("50_states.csv")

# scores
answered_states = []

game_on = True

while game_on and len(answered_states) <= 2:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state name ?")

    if answer_state is None:
        game_on = False
        break

    answer_state = answer_state.title()

    state = state_cors_data[state_cors_data.state == answer_state]

    if not state.empty:
        state_label = turtle.Turtle()
        state_label.hideturtle()
        state_label.penup()
        state_label.goto(int(state.x), int(state.y))
        state_label.write(answer_state)

        screen.update()
        answered_states.append(answer_state)
    else:
        pass


screen.mainloop()
