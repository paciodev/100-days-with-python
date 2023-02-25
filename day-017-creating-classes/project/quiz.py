from os import system

class Quiz:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0
    
    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1

        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ").title()
        self.check_answer(user_answer, question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_answer, answer):
        system('cls')
        if user_answer == answer:
            print('You got it right!')
            print(f"Your answer was: {answer}")
            self.score += 1
        else:
            print("That's wrong.")
            print(f"The correct answer was: {answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print('')