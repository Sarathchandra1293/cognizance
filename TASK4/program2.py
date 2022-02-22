# a program to accept a string from the user and display characters,that are present at an even index number.
#read a string
Enter_the_string = input('enter the string')
#  create a string with characters at multiple of 2
string = Enter_the_string[::2]
print(string)
# it is string slicing method
