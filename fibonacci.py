# fibonacci using a loop
# prev1 = 0
# prev2 = 1
# print(prev1)
# print(prev2)
# for i in range(18):
#     next = prev1+prev2
#     print(next)
#     prev1 = prev2
#     prev2 = next
    
# fibonacci using recursion
# print(0)
# print(1)
# count = 2

# def fibonacci(pre1,pre2):
#     global count
#     if count <=19:
#         new = pre1+pre2
#         print(new)
#         pre1 = pre2
#         pre2 = new
#         count +=1
#         fibonacci(pre1,pre2)
#     else:
#         return 

# fibonacci(1,0)

# return 21st fibonacci number
def F(n):
    if n<=1:
        return n
    else:
        return F(n-1)+F(n-2)
print(F(20))