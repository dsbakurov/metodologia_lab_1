import math
import random


class NOK:
    def __init__(self, n_cycles=5):
        self.name = ""
        self.n_cycles = n_cycles

    def welcome(self):
        print("Welcome to the Brain Games!")
        self.name = input("May I have your name? ")
        print(f"Hello, {self.name}")

    def play(self):
        print("Find the smallest common multiple of given numbers.")
        is_all_correct = True
        for _ in range(self.n_cycles):
            numbers = [random.randint(1, 100) for _ in range(3)]
            print(f"Question: {' '.join(map(str, numbers))}")

            user_answer = int(input("Your answer: "))
            correct_answer = math.lcm(*numbers)
            if user_answer == correct_answer:
                print("Correct!")
            else:
                is_all_correct = False
                print(f"'{user_answer}' is wrong answer ;(. "
                      f"Correct answer was '{correct_answer}'.")
                print(f"Let's try again, {self.name}!")
        if is_all_correct:
            print(f"Congratulations, {self.name}!")

    def start(self):
        self.welcome()
        self.play()


if __name__ == '__main__':
    game = NOK()
    game.start()
