# with open('data/weather.csv') as f:
#     data = f.readlines()
#     print(data)


# import csv
# with open('data/weather.csv') as f:
#     data = csv.reader(f)
#     temperatures = []

#     for row in data:
#         if (row[1] != 'temp'):
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas
# data = pandas.read_csv('data/weather.csv')
# temp_list = data['temp'].to_list()


# avg_temp = sum(temp_list) / len(temp_list)
# avg_temp = data['temp'].mean()

# you can pull data from data by .att or ['att']
# max_temp = data.temp.max()

# print(round(avg_temp, 1))
# print(max_temp)

# max_temp_row = data[data.temp == data['temp'].max()]
# print(max_temp_row)

# monday = data[data.day == 'Monday']
# monday_temp = monday.temp.iloc[0]
# temp_in_fh = monday_temp * 9/5 + 32
# print(temp_in_fh)

data_dict = {
    "students": ["Amy", "James", "Brian"],
    "scores": [76, 65, 1]
}
data = pandas.DataFrame(data_dict)
data.to_csv('data/school.csv')