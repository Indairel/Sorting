
def numbers():
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for num in nums:
        for letter in 'abc':
            print(num, letter)
        if num == 3:
            print('Found!')
            break
            continue
        print(num)

    for i in range(10):
        print(i)

    x = 0
    while x < 1000:
        if x == 5:
            break
        print(x)
        x += 1