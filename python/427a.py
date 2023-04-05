n = int(input())

new = list(map(int, input().split()[:n]))

crimes = 0
polices = 0

for item in new:
    if item > 0:
        polices += item
    if polices > 0 and item < 0:
        polices -= 1
        continue
    if item < 0:
        crimes += 1

print(crimes)