def find_max(list):
    if len(list) == 0:
        return None
    max_value = list[0]
    for num in list:
        if num > max_value:
            max_value = num    
    return max_value

numbers = [5, 4, 8, 1, 12]
print(find_max(numbers)) 