import random

from core import Core


class Progression(Core):
    def ask_question(self):
        progression_len = random.randint(5, 15)
        b = random.randint(1, 5)
        q = random.randint(2, 5)
        numbers = [b * q ** i for i in range(progression_len)]

        answer = random.choice(numbers)

        question = list(map(str, numbers))
        question[numbers.index(answer)] = ".."

        return question, answer
