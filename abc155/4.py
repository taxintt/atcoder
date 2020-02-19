import itertools

# 計算量：愚直に取り組むと  n^2/2
# 思考法：k番目の値(x) -「x未満がk個未満」の条件を満たすxの最大値（x）
# k-1などspecificな言い方をしないのは、xが複数回連続している可能性に対応するため

# 二分探索で調べていく -> x未満が何個存在するかを調べる　
# 片方を固定して、その相方が何個になるかを数える　
# 条件：同じもの2つは選べない

n, k = map(int, input().split())
temp_list = list(map(int, input().split()))

c = itertools.combinations(temp_list, 2)
num_list = sorted(c, key=lambda x: x[0]*x[1])

output_list = list(num_list[k-1])
print(output_list[0] * output_list[1])