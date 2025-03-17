from abc import ABC, abstractmethod


class Core(ABC):
    def __init__(self, n_cycles=3):
        self.name = ""
        self.n_cycles = n_cycles

    def welcome(self):
        print("Welcome to the Brain Games!")
        self.name = input("May I have your name? ")
        print(f"Hello, {self.name}")

    @abstractmethod
    def ask_question(self):
        return 0

    def play(self):
        print("What number is missing in the progression?")
        is_all_correct = True
        for i in range(self.n_cycles):
            question, answer = self.ask_question()
            print(f"Question: {' '.join(question)}")

            user_answer = int(input("Your answer: "))
            if user_answer == answer:
                print("Correct!")
            else:
                is_all_correct = False
                print(f"'{user_answer}' is wrong answer ;(. "
                      f"Correct answer was '{answer}'.")
                print(f"Let's try again, {self.name}!")
        if is_all_correct:
            print(f"Congratulations, {self.name}!")

    def start(self):
        self.welcome()
        self.play()
