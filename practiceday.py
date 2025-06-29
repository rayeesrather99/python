# num = int(input("enter a number: "))

# digit_sum = 0

# while num > 0:
#     digit = num % 10 # gets last digit of num
#     digit_sum += digit
#     num = num // 10

# print(digit_sum)





def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(7))