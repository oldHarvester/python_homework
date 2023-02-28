#Напишите программу нахождения максимума и минимума из трех чисел

def maxNumber(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    if num2 > num1 and num2 > num3:
        return num2
    if num3 > num1 and num3 > num2:
        return num3

def minNumber(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return num1
    if num2 < num1 and num2 < num3:
        return num2
    if num3 < num1 and num3 < num2:
        return num3

num1 = 10
num2 = 40
num3 = 20

print(f'Minimum number: {minNumber(num1, num2, num3)}')
print(f'Maximum number: {maxNumber(num1, num2, num3)}')


