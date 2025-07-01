def has_duplicates(list):
    i = 0
    while i < len(list):
        j = i + 1
        while j < len(list):
            if list[i] == list[j]:
                return True
            j += 1
        i += 1
    return False
print(has_duplicates([1, 2, 3, 4, 5]))   