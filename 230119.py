# coding: utf-8
distance, count = map(int, input().split())
mover = []
arm = []
for i in range(count):
    speed, wait = map(int, input().split())
    if speed == 0:
        arm.append([speed, wait])
    else:
        mover.append([speed, wait])

result = [0] * len(mover)
for ar in arm:
    time = ar[1]
    for i, move in enumerate(mover):
        speed = move[0]
        wait = move[1]
        if result[i] != 0:
            continue
        elif time <= wait:
            continue
        elif distance > speed * (time - wait):
            continue
        else:
            result[i] = time - wait

print(max(result))
