import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game = False

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
guessed_state = []
score = 0

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States correct", prompt="What's another state?")
    ans_state = answer_state.capitalize()

    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to learn.csv")
        break

    if ans_state in state_list:
        score += 1
        guessed_state.append(ans_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_info = data[data.state == ans_state]
        x = int(state_info.x)
        y = int(state_info.y)

        t.goto(x, y)
        t.write(ans_state)

