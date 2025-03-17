import math
import random

from core import Core


class NOK(Core):
    def ask_question(self):
        numbers = [random.randint(1, 100) for _ in range(3)]

        question = map(str, numbers)
        answer = math.lcm(*numbers)

        return question, answer
