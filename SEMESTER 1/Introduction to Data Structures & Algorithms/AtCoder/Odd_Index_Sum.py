n = int(input())
ls = list(map(int, (input().split())))
sum = 0
for i in range(0, len(ls), 2):
    sum += ls[i]
print(sum)