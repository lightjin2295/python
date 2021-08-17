#그리드 탐욕법
#가장큰거부터 정리
#https://www.acmicpc.net/problem/11047

# 10 4200
# 1
# 5
# 10
# 50
# 100
# 500
# 1000
# 5000
# 10000
# 50000

N,K = map(int,input().split())

value =[]
cnt = 0
J = 0
for _ in range(N):
    M = int(input())
    value.append(M)

while K != 0:
    J += K // value[-1]
    K = K % value[-1]
    value.remove(value[-1])
    cnt+=1

print(J)

