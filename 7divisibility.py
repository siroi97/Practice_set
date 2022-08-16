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
xo=int(input('please enter the number of times you want to check the divisibility.'))
for i in range (0,xo):
    x=int(input('please enter a number number'))
    if x%7==0:
        print('The number is Divisible by 7')
    else:
        print('The number is not Divisible by 7')

