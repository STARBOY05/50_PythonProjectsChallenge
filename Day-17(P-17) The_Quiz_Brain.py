
# Importing the questions and it's answer
from data17 import question_data
# Question Model
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
# Putting Question and Answer in a question bank
question_bank = []
for question in question_data:  
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)
# Main QuizBrain 
class QuizBrain:
    # AutoInitialized Model
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    # Printing the new Questions
    def next_question(self):
        curr_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q{self.question_number}: {curr_question.text} (True or False)? >> ")  
        self.check_ans(user_ans,curr_question.answer)
    # Checking if the questions are over
    def still_questions_left(self):
        return self.question_number < len(self.question_list)
    # Checking the answer and giving the score
    def check_ans(self,user_ans,correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("Correct Answer!")
        else:
            print("Wrong Answer!")
        print(f"The correct answer was {correct_ans}.")
        print(f"Your current score is {self.score}/{self.question_number}\n")
    # Displaying the final results
    def final_result(self):
        print("You have completed the Quiz")
        print(f"You have scored {self.score} out of {quiz.question_number} Questions! Well Played 👍")
# Starting the Quiz 
quiz = QuizBrain(question_bank)
# Looping thru the next questions until over
while quiz.still_questions_left():
    quiz.next_question()
# Final Output
quiz.final_result()
