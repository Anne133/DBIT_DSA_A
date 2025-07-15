def selection_sort(unsorted_list):
   
    number_of_items = len(unsorted_list)
    
    for outerloop in range(number_of_items):
        min_index = outerloop
        
        for innerloop in range(outerloop + 1, number_of_items):
            print(f"Minimum is {unsorted_list[min_index]}")
            if unsorted_list[innerloop] < unsorted_list[min_index]:
                min_index = innerloop

        temp = unsorted_list[outerloop]
        unsorted_list[outerloop] = unsorted_list[min_index]
        unsorted_list[min_index] = temp
        print(f"Outerloop {unsorted_list}")
        
        """
        Swap the found minimum element with the first element
        unsorted_list[outerloop], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[outerloop]
         """
    return unsorted_list





values = [5, 4, 3, 2, 1]
print(f"Unsorted list: {values}")
sorted_values = selection_sort(values)
print(f"Sorted list: {sorted_values}")