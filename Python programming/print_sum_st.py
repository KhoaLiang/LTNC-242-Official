def loop1(n):
    i = 1
    sum = 0
    while i <= n:
        sum += i
        i += 1
    return sum
print(str(loop1(int(input()))))