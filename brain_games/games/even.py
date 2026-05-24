from random import randint

from brain_games.games.common import RANDOM_FIRST, RANDOM_LAST


def info():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(number):
    return number % 2 == 0


def get_question():
    random_number = randint(RANDOM_FIRST, RANDOM_LAST)
    question = f'{random_number}'
    correct_answer = 'yes' if is_even(random_number) else 'no'
    return question, correct_answer
