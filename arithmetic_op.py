#Напишите программу которая выводит на экран сумму цифр пятизначного числа

number = 12345;
numberStr = str(number)

sum = 0

for i in range(0, len(numberStr)):
    sum += int(numberStr[i])

print(f'Total sum of number: {sum}')