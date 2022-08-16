#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     16/08/2022
# Copyright:   (c) Admin 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
x=input('Please enter your name')
xq=int(input('Please enter your age'))
if xq<18:
    print('You are not eligible to vote'+ x)
else:
    print('You are eligible to vote '+ x)

