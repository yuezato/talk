# 再帰呼び出しもスタックも使わないバージョン

import copy
import itertools

def R(L):
    l = 0
    N = len(L)
    r = N - 1

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

            if j < r-1: # 右部分リストが存在する
                L[j+1], L[r] = L[r], L[j+1] # 値の交換

            r = j # 左部分リストにとりかかる

        assert(l == r)  # 再帰呼び出しのbase case相当になったので

        if r == N-1:
            return # 回復不要＝計算終了
            
        p = L[r+1]
        # <pの間右に進むことにする
        count = 0
        for idx in range(r+2, N):
            if L[idx] < p:
                count += 1
            else: break
        if count > 0: # 右部分リストがあったことになるので
            L[r+1+count], L[r+1] = L[r+1], L[r+1+count] # 交換する
        l = r+1
        r = r+1 + count

def Q(L):
    L.append(float('inf'))
    R(L)


# 値がM未満の長さsizeのリストを片っ端から生成して
# 正しくソートできているか検証する
        
M = 10
for size in range(0, 8):
    for tup in itertools.product(range(M), repeat=size):
        L = list(tup) 
        orig = copy.deepcopy(L)
        Q(L)
        if sorted(orig) != L[:-1]: # 整列されているかをテスト
            print("Bug:", orig, L)
            return
