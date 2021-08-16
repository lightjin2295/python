from collections import deque

# 백준 2606번. 바이러스
# https://www.acmicpc.net/problem/2606
# BFS를 이용한 바이러스문제


def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    count = 0
    while q:
        v = q.popleft()

        for i in range(N):
            if graph[v][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = 1
                count+= 1
    return count


N = int(input())
M = int(input())
print(M)

graph=[[0]*N for _ in range(N)]
visited = [0 for _ in range(N)]

for _ in range(M):
    x,y = map(int,input().split())
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1



print(bfs(1))

# from collections import deque
#
# def bfs(x):
#     q = deque()
#     q.append(x)
#     visited[x] = 1
#     count = 0
#
#     while q:
#         v = q.popleft()
#
#         for i in range (N):
#             if graph[v][i] == 1 and visited[i] == 0:
#                 q.append(i)
#                 visited[i] = 1
#                 count +=1
#     return count
#
# # def dfs(x):
# #     global cnt
# #     cnt+=1
# #     visited[x] =1
# #
# #     for i range(N):
# #         if graph[v][i] == 1 and vi
#
#
#
# N = int(input())
# M = int(input())
#
# graph = [[0] * N for _ in range(N)]
# visited = [0 for _ in range(N)]
#
# for _ in range(M):
#     x,y = map(int,input().split())
#     graph[x-1][y-1] = 1
#     graph[y-1][x-1] = 1
#
# print(bfs(1))


