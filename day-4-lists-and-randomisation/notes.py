# import random

# random_int = random.randint(1, 10)
# print(random_int)

# random_float = random.random()
# print(random_float)

# love_score = round(random.random() * 100, 2)
# print(f'Your love score is {love_score}')

states_of_usa = ['Delaware', 'Pennsylvania', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Virginia']

print(states_of_usa[0]) # Delaware
print(states_of_usa[-1]) # Virginia

print(states_of_usa[2]) # South Carolina
states_of_usa[2] = 'North Carolina'
print(states_of_usa[2]) # North Carolina

states_of_usa.append('South Carolina') # Add to the end of the list
states_of_usa.extend(['New Mexico', 'Arizona']) # Adding this two items to the end of the list