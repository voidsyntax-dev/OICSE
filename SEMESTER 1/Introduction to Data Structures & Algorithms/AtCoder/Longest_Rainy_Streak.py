curr, high = 0, 0
n = int(input())
s = input()
for weather in s:
    if weather == 'R':
        curr += 1
    else:
        high = max(curr, high)
        curr = 0
print(max(high, curr))