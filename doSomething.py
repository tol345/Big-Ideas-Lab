num1 = int(input("Enter a number:"))
num2 = int(input("Enter another Number:"))

if(num1 > num2):
    print(num1, "is greater then", num2)
elif(num2 > num1):
    print(num2, "is greater then", num1)
else:
    print(num1, "is equal to", num2)
