class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(n)]
        child = [1] * n
        for i in range(n - 1):
            adj[edges[i][0]].append(edges[i][1])
            adj[edges[i][1]].append(edges[i][0])

        def dfs(u, p):
            for v in adj[u]:
                if v == p:
                    continue
                dfs(v, u)

        dfs(0, 0)