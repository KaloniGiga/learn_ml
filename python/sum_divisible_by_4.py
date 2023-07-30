def sum_divisible_by_4():
    sum = 0
    while(True):
        num = int(input('Enter a number'))
        if num % 4 == 0:
            sum = sum + num
        else:
            break
    print(sum)

sum_divisible_by_4()
