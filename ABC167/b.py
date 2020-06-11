A, B, C, K = map(int, input().split())

if K <= A:
    print(K)
    exit()

K -= A+B
if K <= 0:
    print(A)
else:
    print(A-K)
