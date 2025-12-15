lst = list(map(int, input().split()))

for i in lst:
    for j in lst:
        if i < j:
            max = i
            break

print(max)