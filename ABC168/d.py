from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

p=[0]*N
que= deque([0])

while que:
    v=que.popleft()
    for i in graph[v]:
        if p[i]<1:
            p[i]=v+1
            que.append(i)

if 0 in p:
    print("No")
else:
    print("Yes", *p[1:], sep="\n")
