N, K = map(int, input().split())

A = list(map(int, input().split()))

now = 1
B = [0] * N
cycle = -1
bC = -1

if K < N:
    for _ in range(K):
        now = A[now - 1]
    print(now)
    exit()
else:
    for i in range(N+1):
        now = A[now - 1]
        if B[now - 1] == 0:
            B[now - 1] = i
        else:
            cycle = i - B[now - 1]
            bC = B[now - 1] + 1
            break
    last = (K - bC)%cycle
    for _ in range(last):
        now = A[now - 1]
    print(now)
    exit()

