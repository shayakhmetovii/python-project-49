from random import choice, randint

from brain_games.games.common import RANDOM_FIRST, RANDOM_LAST


def info():
    print('What is the result of the expression?')


def get_question():
    operation = choice('+-*')
    random_number1 = randint(RANDOM_FIRST, RANDOM_LAST)
    random_number2 = randint(RANDOM_FIRST, RANDOM_LAST)
    question = f'{random_number1} {operation} {random_number2}'
    correct_answer = ''
    match operation:
        case '+':
            correct_answer = str(random_number1 + random_number2)
        case '-':
            correct_answer = str(random_number1 - random_number2)
        case '*':
            correct_answer = str(random_number1 * random_number2)

    return question, correct_answer
