import prompt

from brain_games.cli import welcome_user

ROUNDS = 3
RANDOM_FIRST = 1
RANDOM_LAST = 100


def welcome():
    print('Welcome to the Brain Games!')


def launch(game):
    welcome()
    user = welcome_user()
    game.info()
    for _ in range(ROUNDS):
        question, correct_answer = game.get_question()
        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let\'s try again, {user}!")
            return
    print(f'Congratulations, {user}!')
