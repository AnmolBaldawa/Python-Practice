"""Write a program which can compute the factorial of a given numbers.The results should be printed in a
comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output
should be:40320 """

factorial = int(input("Enter the number for which factorial is to be found: "))
value = 1
for i in range(1, factorial + 1):
    value *= i
print(value)
