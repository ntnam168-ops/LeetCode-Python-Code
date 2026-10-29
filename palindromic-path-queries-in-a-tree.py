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
		lz = [[0] * 26 for _ in range(4 * n)]
		t = s[:]
		s = list(s)
		t = list(t)
			
		for i in range(n):
			t[in_[i]] = s[i]
			
		def mer(a, b) -> list[int]:
			for i in range(26):
				a[i] += b[i]
				
			return a
			
		def push(node, l, r):
			if not max(lz[node]) or l == r:
				return
				
			for i in range(26):
				lz[node * 2 + 1][i] += lz[node][i]
				lz[node * 2 + 2][i] += lz[node][i]
				lz[node][i] = 0
					 
		def update(node, l, r, x, y, pos, val):
			print(node, l, r, x, y)
			if l > y or r < x:
				return
			if l >= x and r <= y:
				lz[node][pos] += val
				print(node, pos)
				return
			
			md = (l + r) // 2
			update(node * 2 + 1, l, md, x, y, pos, val)
			update(node * 2 + 2, md + 1, r, x, y, pos, val)
		
		def get(node, l, r, pos) -> list[int]:
			push(node, l, r)
			if l > pos or r < pos:
				return [0] * 26
			
			if l == r:
				return lz[node]
				
			md = (l + r) // 2
			
			return mer(get(node * 2 + 1, l, md, pos), get(node * 2 + 2, md + 1, r, pos))

		ans = []
		
		for i in range(n):
			update(0, 0, n - 1, in_[i], ou_[i], ord(s[i]) - ord('a'), 1)
			print(in_[i], ou_[i], ord(s[i]) - ord('a'), 1)
			# print()
			print(get(0, 0, n - 1, 0))
			print(get(0, 0, n - 1, 1))
			print(get(0, 0, n - 1, 2))
			# print()
		
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
				print(x, y, p)
				# print(in_[x], in_[y], in_[p])
				g1 = get(0, 0, n - 1, in_[x])
				g2 = get(0, 0, n - 1, in_[y])
				g3 = get(0, 0, n - 1, in_[p])
				print(g1)
				print(g2)
				print(g3)
				g1[ord(s[p]) - ord('a')] += 1
				res = 0
								
				for i in range(26):
					g1[i] = g1[i] + g2[i] - 2 * g3[i]
					res += g1[i] & 1
					# print(g1[i], end = " ")
				# print()
				
				if res > 1:
					ans.append(False)
				else:
					ans.append(True)
					
			print(tp, x, y)
		return ans

s = Solution()
print(s.palindromePath(3, [[0, 1], [1, 2]], "aac", ["query 0 2", "update 1 b", "query 0 2"]))
print(s.palindromePath(4, [[0, 1], [0, 2],[0, 3]], "abca", ["query 1 2", "update 0 b", "query 2 3", "update 3 a", "query 1 3"]))