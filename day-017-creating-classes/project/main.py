from question import Question
from data import question_data
from quiz import Quiz
from os import system

system('cls')

question_bank = []
for q in question_data:
    question = Question(q['text'], q['answer'])
    question_bank.append(question)

quiz = Quiz(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

system('cls')

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
print('')