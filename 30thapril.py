def power2(number):

    if (number==0):
        return 0
    if (number & (~(number & (number - 1)))):
         return 1
    return 0
    if(count % 2 == 0):
            return True
    else:
            return False
number = int(input("Enter your number : "))

if(power2(number)):
    print("\nThe number is power of 2")
else:
    print("\nThe number is not power of 2")
