def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i  
    return -1  


numbers = [1, 2, 3, 4, 5]
print(f"index:", linear_search(numbers, 3))   
  