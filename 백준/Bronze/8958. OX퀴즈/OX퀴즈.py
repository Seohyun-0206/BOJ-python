n = int(input())

for i in range(n):
    str = input()
    cnt = 0
    result = 0
    for j in str:
        if j == 'O':
            cnt += 1
            result += cnt
        else:
            cnt = 0

    print(result)