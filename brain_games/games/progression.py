from random import randint

MIN_TERMS = 10
MAX_TERMS = 20
MIN = 5
MAX = 15


def info():
    print('What number is missing in the progression?')


def make_progression(initial, difference):
    member_of_progression = initial
    progression = [initial]
    for _ in range(randint(MIN_TERMS, MAX_TERMS)):
        member_of_progression += difference
        progression.append(member_of_progression)
    return progression


def stringify(progression, missing):
    progression_str = []
    for index in range(len(progression)):
        progression_str.append(str(progression[index]))
    progression_str[missing] = '..'
    return " ".join(progression_str)


def get_question():
    initial = randint(MIN, MAX)
    difference = randint(MIN, MAX)
    progression = make_progression(initial, difference)
    missing = randint(1, len(progression) - 1)
    question = stringify(progression, missing)
    correct_answer = str(progression[missing])
    return question, correct_answer
