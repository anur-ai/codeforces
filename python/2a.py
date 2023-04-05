n = int(input())

name_list = []
score_list = []

for i in range(n):
    name,score = input().split()
    if name in name_list:
        score_list[int(name_list.index(name))] += int(score)
    else:
        name_list.append(name)
        score_list.append(int(score))

print(name_list[score_list.index(max(score_list))])
