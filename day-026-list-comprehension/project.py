import pandas
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
alphabet_data = pandas.read_csv('phonetic_alphabet.csv')
alphabet_dict = {row.letter:row.code for (_, row) in alphabet_data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

print('Welcome in NATO Phonetic Alphabet tool.')
print('Please provide a word to check the alphabet for.')
word = input('Word: ').upper()
letters = [*word]
result_dict = {letter:alphabet_dict[letter] for letter in letters}

for (key, val) in result_dict.items():
    print(f"{key} - {val}")