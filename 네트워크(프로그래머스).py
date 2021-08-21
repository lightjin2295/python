from collections import deque

def solution(n, computers):
    
    def DFS(val):
        visited[val] = 1
        
        for i in range(n):
             if computers[val][i] and not visited[i]:
                    DFS(i)
    
    def BFS(val):
        q = deque()
        q.append(val)
        
        while q:
            k = q.popleft()
            visited[k] = 1
            for i in range(n):
                if computers[i][k] == 1 and visited[i] == 0:
                    q.append(i)
        
    
    answer = 0
    visited = [0 for _ in range(n)]
    
    for i in range(n):
        if not visited[i]:
            DFS(i)
            # BFS(i)
            answer+=1    
    
    return answer