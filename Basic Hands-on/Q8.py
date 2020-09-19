'''Write a program that accepts a comma separated sequence of words as input and prints the words in a
comma-separated sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:

without,hello,bag,world
Then, the output should be:

bag,hello,without,world'''

# Method 1
word_list = list(input('Enter words seperated by commas: ').split(','))
word_list.sort()
print(','.join(word_list))

# Method 2
print(','.join(sorted(input('Enter words seperated by commas: ').split(','))))
