# 再帰呼び出しではなく、スタックを使うバージョン

import copy
import itertools

def Q(Stack, L):
    l = 0
    r = len(L)

    while True:
        while l < r:
            pivot = L[l] # 左端をpivotにする
            i = l+1
            j = r-1
            
            # Partitioning part
            while True:
                while i < j and L[i] <  pivot: i += 1
                while l < j and L[j] >= pivot: j -= 1
                if j <= i:
                    break
                else:
                    L[i], L[j] = L[j], L[i] # 値の入れ替え

            L[l] = L[j]
            L[j] = pivot

            Stack.append(r) # pushのつもり
            r = j # 左部分リストにとりかかる

        assert(l == r)  # 再帰呼び出しのbase case相当になったので
        if Stack == []: # もうやることがなければ終了
            return
        else:
            l = r + 1
            r = Stack.pop() # まだやる計算があるなら、それに進む

# 値がM未満の長さsizeのリストを片っ端から生成して
# 正しくソートできているか検証する
            
M = 7
for size in range(0, 8):
    for tup in itertools.product(range(M), repeat=size):
        L = list(tup) # 値がM未満の長さsizeのリストを片っ端から生成
        # print(L)
        orig = copy.deepcopy(L)
        Q([], L)
        if sorted(orig) != L: # 整列されているかをテスト
            print("Bug:", orig)
            return
