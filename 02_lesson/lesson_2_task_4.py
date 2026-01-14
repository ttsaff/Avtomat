n = int(input('Введите число: '))
if n <= 1:
    n = 3

for n in range(1,n):
    string = ' '
    if (n % 3 == 0):
        string = string + "Fizz"
    if (n % 5 == 0):
        string = string + "Buzz"
    if (n % 3 != 0 and n % 5 != 0):
        string = string + str(n)
    print(string, end = '')