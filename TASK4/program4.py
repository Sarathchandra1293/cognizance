# check whether given number is a palindrome
p = int(input('enter the given input: '))
prog = p
rem = 0   # here rem means remainder
rev = 0   # here rev means reverse
while(p!=0):
    rem = p % 10
    p = p//10   # here // denotes integer
    rev = rev * 10 + rem

if(prog == rev):
    print(f' TRUE,{prog} is palindrome number')
else:
    print(f' FALSE,{prog} is not a palindrome number')
