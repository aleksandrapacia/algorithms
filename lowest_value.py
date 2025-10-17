my_array = [7, 12, 9, 4, 11]
minVal = my_array[0]
for each in my_array:
    if each < minVal:
        minVal = each
print("Lowest value: ", minVal)