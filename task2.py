#Найдите сумму цифр трехзначного числа
number = int(input('Введите 3-ех значное число: '))
sum=0
if number//100<1 or number//100>10:
    print('Вы ввели неподходящее число')
else:
    sum=number//100+(number//10)%10+number%100%10
    print(sum)