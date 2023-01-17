# coding: utf-8
string_all = input()
string_part = input()

ans = 0
for i in range(len(string_all) - len(string_part) + 1):
    substr = ""
    # 現サーチポイントから部分文字列サイズを抽出
    for j in range(len(string_part)):
        substr += string_all[i + j]
    if substr == string_part:
        ans += 1

print(ans)
