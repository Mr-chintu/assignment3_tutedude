def factorial(n):
    if n < 2:
        return 1
    return n*factorial(n-1)
x = int(input("Enter a number: "))
fact = factorial(x)
print("Factorial of 5 is:",fact)

# using loops 
# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         for i in range(2,n+1):
#             n*=i-1
#         return n
# result = factorial(5)
# print("Factorial of 5 is:",result)