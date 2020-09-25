from create_list import create_list

# please remember that this sort function can only sort integers not float but does so more efficently using the radix-count sorting algorithm
def sort_list(list):

    def get_digit_counts(list, position, num_repetitions):
        # list that represents digit counts from 0 - 9
        count_list = [0 for i in range(10)]
        # find largest num to know how many iterations we need to do
        first_run = True if not num_repetitions else False
        largest_num = 0 if not num_repetitions else num_repetitions
        for num in list:
            if first_run:
                largest_num = num if num > largest_num else largest_num
            str_num = str(num)
            try:
                digit = int(str_num[-position])
            except IndexError:
                digit = 0
            count_list[digit] += 1
        
        if first_run:
            num_repetitions = len(str(largest_num))
        return count_list, num_repetitions

    def get_element_indices(count_list):
        index_list = [0 for i in range(10)]
        for index, count in enumerate(count_list):
            index_list[index] = count + index_list[index - 1] if index > 0 else count
        return index_list

    def rebuild_list(list, index, position):
        new_list = [0 for i in range(len(list))]
        index_list = index.copy()
        # get value of num at position
        for num in reversed(list):
            str_num = str(num)
            try:
                digit = int(str_num[-position])
            except IndexError:
                digit = 0
            num_position = index_list[digit] - 1
            new_list[num_position] = num
            index_list[digit] -= 1
        return new_list

    largest_num = None
    current_iteration = 1
    while True:
        count_list, largest_num = get_digit_counts(list, current_iteration, largest_num)
        index_list = get_element_indices(count_list)
        list = rebuild_list(list, index_list, current_iteration)
        if largest_num == current_iteration:
            break
        else:
            current_iteration += 1
    
    return list

list = create_list(1_000_000, 100)
sorted_list = sort_list(list)
