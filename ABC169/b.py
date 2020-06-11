N = int(input())

P = list(map(int, input().split()))

out_range = 10**18

ans=1
if  0 in P:
    print(0)
    exit()

for i in range(N):
    tmp = P[i]
    ans *= tmp
    if  ans > out_range:
        print(-1)
        exit()

print(ans)
