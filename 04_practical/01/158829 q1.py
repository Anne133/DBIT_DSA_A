#reversing list
my_list=["a","b","c","d","e"]
my_list.reverse()
print(my_list)

#rotating list
def rotate_list(lst, k):
    n=2
rotated_list= my_list[-2:] + my_list[:-2]
print (rotated_list)
