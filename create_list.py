from random import randint

def create_list(length, parameter):
    random_list = [randint(0, parameter) for _ in range(length)]
    return random_list