from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
index = 1

for data in question_data:
    question_model = Question(data["text"], data["answer"])
    question_bank.append(question_model)

for question in question_bank:
    ask_question = QuizBrain(question.question_data)
    if ask_question.ask_question(index) == question.answer_data:
        print("Congratulations! Your answer is correct")
    else:
        print("Oops! you have entered wrong answer")

    index += 1
