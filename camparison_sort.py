from create_list import create_list

# this sorting algorithm can sort every list, no matter what dtype the numbers are in, but takes alot of computing power to execute on larger arrays 
def sort_list(list, reversed=False):
    i = 0 if not reversed else len(list) - 1
    while True:
        current_item = i
        next_item = current_item + 1 if not reversed else current_item - 1
        if not reversed:
            while list[current_item] > list[next_item]:
                list[current_item], list[next_item] = list[next_item], list[current_item]
                if current_item > 0:
                    current_item -= 1
                    next_item -= 1
            if i < len(list) - 2:
                i += 1
            else:
                break  
                
        if reversed:
            while list[current_item] > list[next_item]:
                list[current_item], list[next_item] = list[next_item], list[current_item]
                if current_item < len(list) - 1:
                    current_item += 1
                    next_item += 1
            if i > 1:
                i -= 1
            else:
                break
    return list

list = create_list(1_000, 100)
print(list)
sorted_list = sort_list(list)
print(sorted_list)

