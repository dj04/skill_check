# coding: utf-8
row, column, column_number, cell_min = map(int, input().split())

csv = []
for i in range(row):
    line = list(map(int, input().split(",")))
    csv.append(line)

for line in csv:
    if line[column_number - 1] >= cell_min:
        print(*line, sep=",")
