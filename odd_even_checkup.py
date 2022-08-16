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
# Odd and Even number checking with range.
xo=int(input('please enter the number of times you want to check.'))
for i in range (0,xo):
    x=int(input('please enter a number number'))
    if x%2==0:
        print('The number is a even number')
    else:
        print('The number is a odd number')

