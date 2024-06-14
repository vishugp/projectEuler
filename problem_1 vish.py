def euler_1(num, muls):
    total = 0
    for i in range(1, num):
        mul_list = [k for k in [i%m for m in muls] if k==0]
        # print(i, mul_list)
        if len(mul_list)>0:
            total+=i
    return total

print(euler_1(1000, [3,5]))





