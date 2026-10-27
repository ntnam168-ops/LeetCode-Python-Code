n = int(input())
adj = [[] for _ in range(n)]
for i in range(n - 1):
    u, v = map(int, input().split())
    adj[u - 1].append(v - 1)
    adj[v - 1].append(u - 1)

dist, res = [0] * n, [0] * n

def dfs(u, p):
    for v in adj[u]:
        if v == p:
            continue
        dfs(v, u)
        dist[u] = max(dist[u], dist[v] + 1)

def dfs1(u, p):
    
    for v in adj[u]:
        if v == p:
            continue

dfs(1, 0)
dfs1(1, 0)

for i in range(n):
    print(res[i], end = " ")