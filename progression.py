import random


class Progression:
    def __init__(self, n_cycles=3):
        self.name = ""
        self.n_cycles = n_cycles

    def welcome(self):
        print("Welcome to the Brain Games!")
        self.name = input("May I have your name? ")
        print(f"Hello, {self.name}")

    def play(self):
        print("What number is missing in the progression?")
        is_all_correct = True
        for i in range(self.n_cycles):
            progression_len = random.randint(5, 15)
            b = random.randint(1, 5)
            q = random.randint(1, 5)
            numbers = [b * q ** i for i in range(progression_len)]

            hidden_number = random.choice(numbers)

            numbers_to_print = list(map(str, numbers))
            numbers_to_print[numbers.index(hidden_number)] = ".."

            print(f"Question: {' '.join(numbers_to_print)}")

            user_answer = int(input("Your answer: "))
            if user_answer == hidden_number:
                print("Correct!")
            else:
                is_all_correct = False
                print(f"'{user_answer}' is wrong answer ;(. "
                      f"Correct answer was '{hidden_number}'.")
                print("Let's try again, Sam!")
        if is_all_correct:
            print("Congratulations, Sam!")

    def start(self):
        self.welcome()
        self.play()


if __name__ == '__main__':
    game = Progression()
    game.start()
