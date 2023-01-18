# coding: utf-8
day_a = int(input())
live_a = [0] * day_a
for i in range(day_a):
    live_a[i] = int(input())

day_b = int(input())
live_b = [0] * day_b
for i in range(day_b):
    live_b[i] = int(input())

liv_i = 0
liv_j = 0

go_live = "A"
for i in range(31):
    today = i + 1
    while live_a[liv_i] < today:
        liv_i += 1
        if liv_i >= len(live_a):
            liv_i -= 1
            break
    while live_b[liv_j] < today:
        liv_j += 1
        if liv_j >= len(live_b):
            liv_j -= 1
            break
    if today != live_a[liv_i] and today != live_b[liv_j]:
        print("x")
    elif today == live_a[liv_i] and today == live_b[liv_j]:
        print(go_live)
        if go_live == "A":
            go_live = "B"
        else:
            go_live = "A"
    elif today == live_a[liv_i]:
        print("A")
    else:
        print("B")

