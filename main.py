import turtle
import pandas

num_states_guessed = 0
screen = turtle.Screen()
screen.title(f"U.S. States Game: {num_states_guessed}/50")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

timmy = turtle.Turtle()
timmy.hideturtle()
timmy.color("black")
timmy.penup()


def write_state_name(state_name, coordinates):
    timmy.goto(coordinates)
    timmy.write(arg=state_name, align="left", font=("Verdana", 10, "bold"))


data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()

guessed_states = []

while num_states_guessed != 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What is another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        break
    if answer_state in states_list and answer_state not in guessed_states:
        row = data[data.state == answer_state]  # DataFrame
        xcor = row.iloc[0, 1]
        ycor = row.iloc[0, 2]
        location = (xcor, ycor)
        write_state_name(answer_state, location)
        guessed_states.append(answer_state)
        num_states_guessed += 1
        screen.title(f"U.S. States Game: {num_states_guessed}/50")


missing_states = []

for state in states_list:
    if state in states_list and state not in guessed_states:
        missing_states.append(state)

print(missing_states)
print(len(missing_states))

new_data = pandas.DataFrame(missing_states)
new_data.to_csv("states_to_learn.csv")

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# Used to get the pixel coordinates of each state in the blank_states_img.gif
# Will print the coordinate location of where the user clicked on the image
