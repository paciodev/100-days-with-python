print('Welcome to the rollercoaster!')

height = int(input('What is your height in cm? '))
bill = 0

if height > 120:
    age = int(input('What is your age? '))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    elif age >= 45 and age <= 55:
        bill = 0
    else:
        bill = 12
    wants_photo = input('Do you want a photo taken? Y or N: ')
    if wants_photo == "Y":
        bill += 3
    print(f'You have to pay ${bill}')
else:
    print('Sorry, you have to grow taller before you can!')
