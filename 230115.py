array_all_count, array_part_count = map(int, input().split())
array_all = list(map(int, input().split()))
array_part = list(map(int, input().split()))

find_out_count = 0
for value_part in array_part:
    for value_all in array_all:
        if value_all == value_part:
            find_out_count += 1
            break

if find_out_count == array_part_count:
    print("Yes")
else:
    print("No")


# n, m = map(int, input().split())
# a = [int(x) for x in input().split()]
# b = [int(x) for x in input().split()]
#
# match_count = 0
# for i in range(n):
#     if a[i] == b[match_count]:
#         match_count += 1
#     if match_count == m:
#         print("Yes")
#         break
# elseブロックが処理されるのは、「breakでループを抜けなかった時」です。厳密に言うと「ループを一度も実行しなかった時」も含まれます。
# else:
#     print("No")