def OddOccurring(arr):

    # Initialize result
    res = 0
for element in arr:
    res = res ^ element

    return res

arr = []

# Take array size as input
n = int(input("Enter array size : "))

while(n):
    num = int(input("Enter number : "))
    arr.append(num)
    n-=1

print("\n\nOdd occurring number is : ",OddOccurring(arr))