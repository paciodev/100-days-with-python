############ DEBUGGING EXAMPLES #####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20): # second number is omitted so "i" is never equal to 20
#     if i == 20: # set this to 19 or change range to (1, 21) to make this code to work
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) # array has not image of index equal to 6 so when dice_num = 6 code crashes
# print(dice_imgs[dice_num]) # set dice num to randint(0, 5) to make this code fully work

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994: # set > to >= to make this code work
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?") # set type of "age" to int()
# if age > 18:
# print("You can drive at age {age}.") # indent this and change it from normal string to "f string"

# # Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) # change double equal sign to normal one
# total_words = pages * word_per_page
# print(total_words)

# # Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item) # indent this
#   print(b_list)

# mutate([1,2,3,5,8,13])