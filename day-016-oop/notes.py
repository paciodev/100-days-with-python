# from turtle import Turtle, Screen

# window = Screen()
# bob = Turtle()

# bob.shape('turtle')
# bob.color('#0000aa')

# bob.forward(100)

# window.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.align = 'l'

table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])

print(table)
