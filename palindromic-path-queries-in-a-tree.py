import sys
sys.setrecursionlimit(10 ** 5)

class Solution:
	def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
		adj = [[] for _ in range(n)]
		
		for [u, v] in edges:
			adj[u].append(v)
			adj[v].append(u)
			
		idx, in_, ou_ = -1, [0] * n, [0] * n
		h, pa = [0] * n, [[-1] * 16 for _ in range(n)]
		
		def dfs(u, p):
			nonlocal idx
			idx += 1
			in_[u] = idx
			
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
		lz = [0] * (4 * n)
		t = s[:]
		s = list(s)
		t = list(t)
			
		for i in range(n):
			t[in_[i]] = s[i]
			
		def push(node, l, r):
			if l == r:
				return
				
			lz[node * 2 + 1] ^= lz[node]
			lz[node * 2 + 2] ^= lz[node]
			lz[node] = 0
					 
		def update(node, l, r, x, y, pos, val):
			if l > y or r < x:
				return
			if l >= x and r <= y:
				lz[node] ^= val
				return
			
			md = (l + r) // 2
			update(node * 2 + 1, l, md, x, y, pos, val)
			update(node * 2 + 2, md + 1, r, x, y, pos, val)
		
		def get(node, l, r, pos) -> int:
			push(node, l, r)
			
			if l == r:
				return lz[node]
				
			md = (l + r) // 2
			
			if md >= pos:
				return get(node * 2 + 1, l, md, pos)
			return get(node * 2 + 2, md + 1, r, pos)

		ans = []
		
		for i in range(n):
			update(0, 0, n - 1, in_[i], ou_[i], 1 << (ord(s[i]) - ord('a')), 1)
		
		for que in queries:
			tp, x, y = que.split()
			
			if tp == "update":
				x = int(x)
				update(0, 0, n - 1, in_[x], ou_[x], ord(s[x]) - ord('a'), -1)
				s[x] = y[0]
				update(0, 0, n - 1, in_[x], ou_[x], ord(s[x]) - ord('a'), 1)
			else:
				x, y = int(x), int(y)
				p = lca(x, y)
				g1 = get(0, 0, n - 1, in_[x])
				g2 = get(0, 0, n - 1, in_[y])
				g3 = get(0, 0, n - 1, in_[p])
				g1[ord(s[p]) - ord('a')] += 1
				res = 0
								
				for i in range(26):
					g1[i] = g1[i] + g2[i] - 2 * g3[i]
					res += g1[i] & 1
				
				if res > 1:
					ans.append(False)
				else:
					ans.append(True)
					
		return ans
		
s = Solution()
print(s.palindromePath(3, [[0,1],[1,2]], "aac", ["query 0 2","update 1 b","query 0 2"]))