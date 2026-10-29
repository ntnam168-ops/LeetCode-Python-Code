import sys
sys.setrecursionlimit(10 ** 5)

class Solution:
	def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
		adj = [[] for _ in range(n)]
		for [u, v] in edges:
			adj[u].append(v)
			adj[v].append(u)
		idx, in_, ou_ = 0, [0] * n, [0] * n
		
		def dfs(u, p):
			nonlocal idx
			in_[u] = idx
			idx += 1
			for v in adj[u]:
				if v == p:
					continue
				dfs(v, u)
			ou[u] = idx
	
		dfs(0, 0)
		return 1

s = Solution()
print(s.palindromePath(3, [[0, 1], [1, 2]], "aac", ["query 0 2", "update 1 b", "query 0 2"]))
print(s.palindromePath(4, [[0, 1], [0, 2],[0, 3]], "abca", ["query 1 2", "update 0 b", "query 2 3", "update 3 a", "query 1 3"]))