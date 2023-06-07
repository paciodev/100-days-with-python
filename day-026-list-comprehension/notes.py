# numbers = [1, 2, 3]
# larger_numbers = [num + 1 for num in numbers]
# print(larger_numbers)

# name = "Patryk"
# name_splitted = [letter for letter in name]
# print(name_splitted)

# challange = [(num + 1) * 2 for num in range(0, 5)]
# print(challange)

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# short_names = [name for name in names if len(name) <= 4]
# print(short_names)

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# long_names_cap = [name.upper() for name in names if len(name) >= 5]
# print(long_names_cap)

# import random
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# students_scores = {name:random.randint(0, 100) for name in names}
# passed_students = {name:score for (name, score) in students_scores.items() if score >= 50}
# print(passed_students)

import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score" : [56, 76, 98] 
}
student_data_frame = pandas.DataFrame(student_dict)
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)