def average(array):
    total = 0
    for value in array:
        total += value
    return total / (len(array))


people, song = map(int, input().split())

rank = []
for i in range(people):
    rank.append(list(map(int, input().split())))

rank_average = [0] * people

for i, p_rank in enumerate(rank):
    rank_average[i] = average(p_rank)

rank_average_sort = sorted(rank_average)

rank_all = [0] * people
for i, av in enumerate(rank_average):
    for j, av_s in enumerate(rank_average_sort):
        if av_s == av:
            rank_all[i] = j + 1
            break

revival = 0
for i, p_rank in enumerate(rank):
    p_rank_min = min(p_rank)
    if rank_all[i] > 3 >= p_rank_min:
        revival += 1
print(revival)
