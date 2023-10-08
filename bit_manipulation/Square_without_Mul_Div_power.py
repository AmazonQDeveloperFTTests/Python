"""
Author  : Gayatri Vadaparty
Date    : October 8,2023

Task:
Given a positive int number. Return Square of that number without Multiplication, Division & Power

Implementation notes: Use bit manipulation.
>>findSquare(6)
36
>>findSquare(-17)
289

"""
def findSquare(number : int) -> int:
    if number < 0:
        square=0
        for _ in range(abs(number)):
            square+= abs(number)
        return square
        
        
    else:
        square=0
        for _ in range(number):
            square+=number
        return square

print(findSquare(0))