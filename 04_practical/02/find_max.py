def find_min(list):
    if len(list) == 0:
        return None
    min_value = list[0]
    for num in list:
        if num < min_value:
            min_value = num    
    return min_value

numbers = [5, 4, 8, 1, 12]
print(find_min(numbers)) 