def bubble_sort(unsorted_list): 
    number_of_items = len(unsorted_list)
    for outerloop in range(number_of_items):
        for innerloop in range(number_of_items - 1 - outerloop):
            if unsorted_list[innerloop] > unsorted_list[innerloop + 1]:
                temp= unsorted_list[innerloop]
                unsorted_list[innerloop] = unsorted_list[innerloop + 1]
                unsorted_list[innerloop + 1] = temp
                # swap the values
                #unsorted_list[innerloop], unsorted_list[innerloop + 1] = unsorted_list[innerloop + 1], unsorted_list[innerloop]
#swap using temp
#temp = a
#a=b
#b= temp

#swap without temp keyword
#print(f"Before A is{a} Bis {b}")
#a,b =b,a
#print(f"After A is{a} Bis {b}")




values = [5, 4, 3, 2, 1]
print(f"Unsorted list: {values}")
sorted_values = bubble_sort(values)
print(f"Sorted list: {sorted_values}")