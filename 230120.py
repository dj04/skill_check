# coding: utf-8
line_count, min_data = map(int, input().split())
# csv_str = [input() for _ in range(line_count)]
csv = []
for i in range(line_count):
    line = list(map(int, input().split(",")))
    csv.append(line)

for csv_line in csv:
    if csv_line[1] >= min_data:
        print(*csv_line, sep=",")
        # print(csv_line[0], end="")
        # for j in range(len(csv_line) - 1):
        #     print("," + str(csv_line[j + 1]), end="")
        # print("")
