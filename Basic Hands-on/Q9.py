'''Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:

Hello world
Practice makes perfect
Then, the output should be:

HELLO WORLD
PRACTICE MAKES PERFECT'''

print('Enter any multi-line sentence and when done, just press enter on empty line')
total = []
while True:
    line = input()
    if len(line) == 0:
        break
    total.append(line.upper())

for line in total:
    print(line)
