import prompt


def welcome_user():
    user = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user))
    return user
