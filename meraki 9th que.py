# Write a code, that counts the numbers between 20 and 40 and then print its 
# count.
numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
list_length=len(numbers)
index=0
less_than_40=0
greater_than_20=0
while index<len(numbers):
    if numbers[index]<40:
        less_than_40+=1
    else:
        greater_than_20+=1
    index+=1
print("less_than_40",str(less_than_40))
print("greater_than_20",str(greater_than_20)) 
     

