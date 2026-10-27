class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(n)]
        child, dis = [1] * n, [0] * n
        for i in range(n - 1):
            adj[edges[i][0]].append(edges[i][1])
            adj[edges[i][1]].append(edges[i][0])

        def dfs(u, p):
            for v in adj[u]:
                if v == p:
                    continue
                dfs(v, u)
                child[u] += child[v]
                dis[u] += dis[v] + child[v]

        dfs(0, 0)