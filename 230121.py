# coding: utf-8
count, radius = map(int, input().split())

for i in range(count):
    tate, yoko, takasa = map(int, input().split())
    if tate >= radius * 2 and yoko >= radius * 2 and takasa >= radius:
        print(i + 1)
