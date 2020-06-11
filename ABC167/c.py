from itertools import combinations
N, M, X = map(int, input().split())

Books = []
for _ in range(N):
    Books.append(list(map(int, input().split())))

ans = 10**9
for i in range(1, N+1):
    for j in combinations(Books, i):
        understand = [0] * M
        cost = 0
        for book in j:
            cost += book[0]
            for p in range(M):
                understand[p] += book[p+1]
        if all(understand[p] >= X for p in range(M)):
            ans = min(ans, cost)

if ans == 10**9:
    print(-1)
else:
    print(ans)




