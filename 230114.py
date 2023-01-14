def insertion_sort(array):
    for i in range(len(array) - 1):
        # // A[i] を、整列済みの A[0] ~ A[i-1] の適切な位置に挿入する

        # // 実装の都合上、A[i] の値が上書きされてしまうことがあるので、予め A[i] の値をコピーしておく
        check = array[i + 1]

        # // A[i] の適切な挿入位置を表す変数 j を用意
        j = i

        # // A[i] の適切な挿入位置が見つかるまで、A[i] より大きい要素を1つずつ後ろにずらしていく
        while j >= 0 and array[j] > check:
            array[j+1] = array[j]
            j -= 1

        # // A[i] を挿入
        array[j + 1] = check

        # // A[0] ~ A[i] が整列済みになった
        print(' '.join(map(str, array)))  # 区切り文字を「 」にして文字列に変換


array_size = int(input())
# map関数を用いて、リストのデータ型を変換
# 戻り値はmap型になるので、listに変換
array = list(map(int, input().split()))
insertion_sort(array)
