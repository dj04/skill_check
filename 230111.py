people = int(input())

max_bat_avg = 0
max_bat_score = 0
max_home_run = 0
result = "Nobody"
for i in range(people):
    bat_avg, bat_score, home_run = map(float, input().split())

    if max_bat_avg <= bat_avg and max_bat_score <= bat_score and max_home_run <= home_run:
        result = "Triple"
    elif (max_bat_avg <= bat_avg and max_bat_score <= bat_score) or\
            (max_bat_avg <= bat_avg and max_home_run <= home_run) or\
            (max_bat_score <= bat_score and max_home_run <= home_run):
        result = "Double"
    elif max_bat_avg < bat_avg or max_bat_score < bat_score or max_home_run < home_run:
        result = "Nobody"
    if max_bat_avg < bat_avg:
        max_bat_avg = bat_avg
    if max_bat_score < bat_score:
        max_bat_score = bat_score
    if max_home_run < home_run:
        max_home_run = home_run

print(result)



# n = int(input())
#
# b = [0] * n
# r = [0] * n
# h = [0] * n
# for i in range(n):
#     x, y, z = input().split()
#     b[i] = float(x)
#     r[i] = int(y)
#     h[i] = int(z)
# flag = [0] * n
# max_b = max(b)
# max_r = max(r)
# max_h = max(h)
# for i in range(n):
#     if b[i] == max_b:
#         flag[i] += 1
#     if r[i] == max_r:
#         flag[i] += 1
#     if h[i] == max_h:
#         flag[i] += 1
#
# if max(flag) == 3:
#     print("Triple")
# elif max(flag) == 2:
#     print("Double")
# else:
#     print("Nobody")
#