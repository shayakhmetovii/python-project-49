from random import randint

from brain_games.games.common import RANDOM_FIRST, RANDOM_LAST


def info():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2
    return True


def get_question():
    random_number = randint(RANDOM_FIRST, RANDOM_LAST)
    question = f'{random_number}'
    correct_answer = 'yes' if is_prime(random_number) else 'no'
    return question, correct_answer
