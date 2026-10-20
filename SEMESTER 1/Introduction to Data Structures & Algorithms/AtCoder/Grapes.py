n, m = map(int, input().split())
k = m // n
print(f"{k+1}\n"*(m%n), end="")
print(f"{k}\n"*(n-m%n))