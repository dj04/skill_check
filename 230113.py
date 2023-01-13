# coding: utf-8
gomoku = [0] * 5
for i in range(5):
    gomoku[i] = input()

result = "D"

check_list = ["O", "X"]
for check in check_list:
    # 横一列
    for line in gomoku:
        win = ""
        for foal in line:
            if foal != check:
                win = "None"
                break
        if win != "None":
            result = check
            break
    if result != "D":
        break
    # 縦一列
    for i in range(5):
        win = ""
        for j in range(5):
            if gomoku[j][i] != check:
                win = "None"
                break
        if win != "None":
            result = check
            break
    if result != "D":
        break
    # 斜め
    if (gomoku[0][0] == check and\
        gomoku[1][1] == check and\
        gomoku[2][2] == check and\
        gomoku[3][3] == check and\
        gomoku[4][4] == check) or\
       (gomoku[0][4] == check and\
        gomoku[1][3] == check and\
        gomoku[2][2] == check and\
        gomoku[3][1] == check and\
        gomoku[4][0] == check):
        result = check
        break

print(result)

# board = []
#
# for i in range(5):
#     board.append(input())
#
#
# def row():
#     result = "D"
#
#     for line in board:
# 最初の1つ目の駒と同じであれば良い
# OとX両方調べる必要なし
#         pivot = line[0]
#         count = 0
#
#         for stone in line:
#             if stone != "." and stone == pivot:
#                 count += 1
#             else:
#                 break
#
#         if count == 5:
#             result = pivot
#             break
#
#     return result
#
#
# def column():
#     result = "D"
#
#     for i in range(5):
#         pivot = ""
#         count = 0
#
#         for j in range(5):
#             if pivot == "":
#                 pivot = board[j][i]
#
#             stone = board[j][i]
#             if stone != "." and stone == pivot:
#                 count += 1
#             else:
#                 break
#
#         if count == 5:
#             result = pivot
#             break
#
#     return result
#
#
# def oblique():
#     result = "D"
#     direction = [True, False]
#
#     for reverse in direction:
#         pivot = ""
#         count = 0
#
#         if reverse:
#             j = 0
#             j_diff = 1
#         else:
#             j = 4
#             j_diff = -1
#
#         for i in range(5):
#
#             stone = board[i][j]
#
#             if pivot == "":
#                 pivot = stone
#
#             if stone != "." and stone == pivot:
#                 count += 1
#
#             j = j + j_diff
#
#         if count == 5:
#             result = pivot
#             break
#
#     return result
#
#
# row = row()
# column = column()
# oblique = oblique()
#
# if row != "D":
#     print(row)
# elif column != "D":
#     print(column)
# elif oblique != "D":
#     print(oblique)
# else:
#     print("D")