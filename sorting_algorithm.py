import random

def create_list(length, parameter):
    digits = [i for i in range(parameter)]
    random_list = random.choices(digits, k=length)
    return random_list

def sort_list(list):
    i = 0
    while True:
        current_item = i
        next_item = current_item + 1
        while list[current_item] > list[next_item]:
            list[current_item], list[next_item] = list[next_item], list[current_item]
            if current_item > 0:
                current_item -= 1
                next_item -= 1
        if i < len(list) - 2:
            i += 1
        else:
            break
    return list

list = create_list(100, 100)
print(sort_list(list))

