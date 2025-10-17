# BUBBLE SORT - sorts an array from the lowest 
# value to the highest value

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        alreay_sorted = True
        for j in range(n-1-i):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1], array[j]
                already_sorted=False
        if already_sorted:
            break

    return array

print('Sorted: ', bubble_sort(my_array))