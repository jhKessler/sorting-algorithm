import random

def create_list(length, parameter):
    digits = [i for i in range(parameter)]
    random_list = random.choices(digits, k=length)
    return random_list