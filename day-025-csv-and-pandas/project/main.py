from turtle import *
import pandas

title('U.S. States Game - type "exit" to exit the game.')

image = 'project/blank_states_img.gif'
addshape(image)
shape(image)

data = pandas.read_csv('project/50_states.csv')
list_of_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = textinput(title=f'{len(guessed_states)}/50 States Correct', prompt="What's another state's name?").title()
    
    if answer_state == 'Exit':
        missing_states = []
        for state in list_of_states:
            if state not in guessed_states:
                missing_states.append(state)
        missing_states_dict = {"state": missing_states}
        new_data = pandas.DataFrame(missing_states_dict)
        new_data.to_csv('project/states_to_learn.csv')
        break

    if answer_state in list_of_states:
        state = data[data.state == answer_state]
        x = state.x.iloc[0]
        y = state.y.iloc[0]
        
        text = Turtle()
        text.hideturtle()
        text.penup()
        text.goto(x, y)
        text.write(answer_state)

        guessed_states.append(answer_state)