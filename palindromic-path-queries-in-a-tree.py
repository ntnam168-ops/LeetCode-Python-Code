import sys
sys.setrecursionlimit(10 ** 5)

class Solution:
	def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
		adj = [[] for _ in range(n)]
		
		for [u, v] in edges:
			adj[u].append(v)
			adj[v].append(u)
			
		idx, in_, ou_ = 0, [0] * n, [0] * n
		h, pa = [0] * n, [[-1] * 16 for _ in range(n)]
		
		def dfs(u, p):
			nonlocal idx
			in_[u] = idx
			idx += 1
			
			for v in adj[u]:
				if v == p:
					continue
					
				h[v] = h[u] + 1
				pa[v][0] = u
				
				for i in range(1, 16):
					pa[v][i] = pa[pa[v][i - 1]][i - 1]
					if pa[v][i] == -1:
						break
						
				dfs(v, u)
				
			ou_[u] = idx
	
		def lca(u, v) -> int:
			if h[u] < h[v]:
				u, v = v, u
				
			for i in range(15, -1, -1):
				if pa[u][i] != -1 and h[pa[u][i]] >= h[v]:
					u = pa[u][i]
					
			if u == v:
				return u
				
			for i in range(15, -1, -1):
				if pa[u][i] != pa[v][i]:
					u, v = pa[u][i], pa[v][i]
					
			return pa[u][0]
				
		h[0] = 1
		dfs(0, 0)
		seg = [[0] * 26 for _ in range(4 * n)]
		lz = [[0] * 26 for _ in range(4 * n)]
		t = s[:]
		t = list(t)
		
		for i in range(n):
			t[in_[i]] = s[i]
		
		def build(node, l, r):
			if l == r:
				seg[node][ord(t[l]) - ord('a')] = 1
				return
			md = (l + r) // 2
			build(node * 2, l, md)
			build(node * 2 + 1, md + 1, r)
			for i in range(26):
				seg[node][i] = seg[node * 2][i] + seg[node * 2 + 1][i]
				 
		
		build(0, 0, n - 1)	
		
		return 1

s = Solution()
print(s.palindromePath(3, [[0, 1], [1, 2]], "aac", ["query 0 2", "update 1 b", "query 0 2"]))
print(s.palindromePath(4, [[0, 1], [0, 2],[0, 3]], "abca", ["query 1 2", "update 0 b", "query 2 3", "update 3 a", "query 1 3"]))