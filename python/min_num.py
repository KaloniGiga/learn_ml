def min_num(num1, num2, num3):
    if num1 > num2:
        if(num2 > num3):
            print('Min num is:', num3)
        else:
            print('Min num is:', num2)
    else:
        if num1 > num3:
            print('Min num is:', num3)
        else:
            print('Min num is:', num1)


min_num(2394, 1984, 1023)