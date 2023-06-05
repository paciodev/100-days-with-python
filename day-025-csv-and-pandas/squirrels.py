# Task with squirrel data
import pandas

sq_data = pandas.read_csv('data/squirrels.csv')
colors = ['Gray', 'Cinnamon', 'Black']
final_dict = {
    "Fur Color": [],
    "Count": []
}

for color in colors:
    count = len(sq_data[sq_data['Primary Fur Color'] == color])
    final_dict['Fur Color'].append(color)
    final_dict['Count'].append(count)

data = pandas.DataFrame(final_dict)
data.to_csv('data/colors_of_squirrels.csv')