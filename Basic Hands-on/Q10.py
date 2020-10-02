"""Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again
Then, the output should be:

again and hello makes perfect practice world"""

# Method 1
wordsList = list(input("Enter space separated words, includes duplicates: ").split(" "))
print(" ".join(sorted(set(wordsList))))

# Method 2
print(" ".join(sorted(set(input("Enter space separated words, includes duplicates: ").split(" ")))))
