class QuizBrain:

    def __init__(self, question):
        self.question_number = 0
        self.question_list = question

    def ask_question(self, index):
        answer = input(f"Q.{index}.{self.question_list}?(True/False) ")
        return answer
