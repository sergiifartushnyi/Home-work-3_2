def move_last_to_front(input_list):

    if len(input_list) <= 1:
        return input_list

    return [input_list[-1]] + input_list[:-1]


print(move_last_to_front([12,3,4,10]))
print(move_last_to_front([1]))
print(move_last_to_front([]))
print(move_last_to_front([12,3,4,10,8]))