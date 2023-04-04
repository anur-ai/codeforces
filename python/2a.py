n = int(input())

name_list = []
score_list = []

for i in range(n):
    name,score = input().split()
    name_list.append(name)
    score_list.append(int(score))

print(name_list[score_list.index(max(score_list))])
