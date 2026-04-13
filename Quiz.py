class Quiz:
    def __init__(self):
        self.questions = ["5+3", "Which  is  the largest Planet?"]
        self.options = [["A. 6", "B. 8", "C. 3"], ["A. Earth", "B. Mars", "C. Jupiter"]]
        self.correct_answers = ["B", "C"]
        self.score = 0

    def start_quiz(self):
        for i in range(len(self.questions)):
            print("\nQuestion", i + 1, ":", self.questions[i])
            for opt in self.options[i]:
                print(opt)
            while True:
                try:
                    user_ans = input("Select an option (A/B/C): ").upper()

                    if user_ans not in ["A", "B", "C"]:
                        raise ValueError("Invalid option! Please enter A, B, or C.")

                    if user_ans == self.correct_answers[i]:
                        self.score += 1
                    break

                except ValueError as e:
                    print(e)

        print("\nQuiz Completed!")
        print("Your Final Score is:", self.score, "/", len(self.questions))
my_quiz = Quiz()
my_quiz.start_quiz()
