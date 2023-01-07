dora_count, group_count = map(int, input().split())

max_dora = []
total_dora = []
for i in range(dora_count):
    max_dora.append(int(input()))
    total_dora.append(0)

dora_now = -1
for i in range(group_count):
    people = int(input())
    for j in range(10000):
        dora_now = (dora_now + 1) % dora_count
        if max_dora[dora_now] >= people:
            total_dora[dora_now] += people
            break
        else:
            total_dora[dora_now] += max_dora[dora_now]
            people -= max_dora[dora_now]

for i in range(dora_count):
    print(total_dora[i])
