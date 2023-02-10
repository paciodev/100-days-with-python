# Tip calculator
print('Welcome to the tip calculator by Pacio!')

total_bill = float(input('What was the total bill? $ '))
tip = float(input('What percentage tip would you like to give? '))
people_to_split = int(input('How many people to split the bill? '))

bill_with_tip = total_bill + total_bill * tip / 100
bill_per_person = round(bill_with_tip / people_to_split, 2)
print(f'Each person should pay: ${bill_per_person}')
