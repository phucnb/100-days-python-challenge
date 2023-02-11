class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)?: ")
        self.check_answer(answer)
        self.question_number += 1
    
    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer):
        if answer.lower() == self.question_list[self.question_number].answer.lower():
            self.score += 1
            print("You got it right!") 
        else:
            print("That's wrong.")
        print(f"Your current score is : {self.score}/{self.question_number + 1}")
        print()
