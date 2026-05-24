from math import gcd
from random import randint

from brain_games.games.common import RANDOM_FIRST, RANDOM_LAST


def info():
    print('Find the greatest common divisor of given numbers.')


def get_question():
    random_number1 = randint(RANDOM_FIRST, RANDOM_LAST)
    random_number2 = randint(RANDOM_FIRST, RANDOM_LAST)
    correct_answer = str(gcd(random_number1, random_number2))
    question = f'{random_number1} {random_number2}'
    return question, correct_answer
