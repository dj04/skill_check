# coding: utf-8
def update(max_value, now_value):
    if max_value < now_value:
        return now_value
    else:
        return max_value


_, check_min = map(int, input().split())
sequence = list(map(int, input().split()))

max_long = 0
now_long = 0
for intger in sequence:
    if intger >= check_min:
        now_long += 1
        max_long = update(max_long, now_long)
    else:
        max_long = update(max_long, now_long)
        now_long = 0

print(max_long)
