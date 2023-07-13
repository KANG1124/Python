# odd and even
number = int(input("Which number do you want to check?"))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# Leap Year
year = int(input("Which year do you want to check"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")

# FizzBuzz
for num in range(1,101):
    if number % 3 == 0 or num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)