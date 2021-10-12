# Write a code, that counts the numbers between 20 and 40 and then print its 
# count.

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# list_length=len(numbers)
# index=0
# less_than40=0
# greater_than20=0
# while index < len(numbers):
#     marks=numbers[index]
#     if numbers<40:
#         less_than40+=1
#     else:
#         greater_than20+=1
# print("marks greater than 20:"+str(greater_than20))
# print("marks less than 40:"+str(less_than40))



string=input("enter the string:")
i=0
while i<len(string):
    j=0
    while j<=i:
        print(string[j],end=" ")
        j+=1
    i+=1
    print()
    
