# coding: utf-8
import math


def is_num(s):
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True


people, answer_count = map(int, input().split())

answer = []
for i in range(people):
    ans = []
    people_answer = input().split()
    for per_answer in people_answer:
        if is_num(per_answer):
            temp = int(per_answer)
            if temp < 0 or 100 < temp:
                ans.append(-1)
            else:
                ans.append(int(per_answer))
        else:
            ans.append(-1)
    answer.append(ans)

total = []
for i in range(answer_count):
    total.append([0, 0])
for i in range(people):
    for j in range(answer_count):
        ans = answer[i][j]
        if ans != -1:
            total[j][0] += 1
            total[j][1] += ans

for to in total:
    print(math.floor(to[1]/to[0]))
