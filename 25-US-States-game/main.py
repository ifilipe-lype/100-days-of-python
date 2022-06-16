import turtle

US_IMG_PATH = "blank_states_img.gif"

screen = turtle.Screen()

# screen setup
screen.title("U.S. States Game")
screen.addshape(US_IMG_PATH)

turtle.shape(US_IMG_PATH)

answer_state = screen.textinput(title="Guess the state", prompt="What's another state name ?");

print(answer_state)


screen.mainloop()