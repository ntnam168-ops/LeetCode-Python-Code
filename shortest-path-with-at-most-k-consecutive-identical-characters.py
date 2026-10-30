class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
 		
s = Solution()
print(s.shortestPath(3, [[0,1,1],[1,2,1],[0,2,3]], "aab", 1))
print(s.shortestPath(3, [[0,1,1],[1,2,1],[0,2,3]], "aab", 2))
print(s.shortestPath(3, [[0,1,1],[1,2,1]], "aaa", 2))