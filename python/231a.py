n = int(input())

s = 0

for i in range(n):
    a,b,c = input().split()
    sum = int(a) + int(b) + int(c)

    if sum >=2:
        s += 1

print(s)