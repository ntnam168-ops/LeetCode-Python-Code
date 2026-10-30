import heapq

class Solution:
	def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
		adj = [[] for _ in range(n)]
		dp = [[10 ** 9] * (k + 1) for _ in range(n)]
		pq = [(0, 0, 1)]
		dp[0][1] = 0
		
		for [u, v, w] in edges:
			adj[u].append([v, w])
		
		while pq:
			d, u, p = heapq.heappop(pq)
			if d != dp[u][p]:
				continue
			for [v, w] in adj[u]:
				val = d + w
				cnt = p
				if labels[u] == labels[v]:
					cnt += 1
				else:
					cnt = 1
				if cnt > k:
					continue
				if dp[v][cnt] > val:
					dp[v][cnt] = val
					heapq.heappush(pq, (val, v, cnt))
			
		res = min(dp[n - 1])
		if res == 10 ** 9:
			res = -1
		return res