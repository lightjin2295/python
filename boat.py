#프로그래머스 구명보트
#https://programmers.co.kr/learn/courses/30/lessons/42885
#해당풀이는 큐를이용해서 가벼운사람과 무거운사람이 limit안에 해당되면 둘다 빼버리고 ++하는

from collections import deque
people = [70,50,50,50,80,50]

q = deque(people)

# [30,40,50,50,70,80]
# [70,100,70,80]
limit = 200
people.sort()
cnt = 0


while q:
    if len(q) >= 2:
        if q[0] + q[-1] <= limit:
            q.pop()
            q.popleft()
            cnt+=1
        elif q[0] + q[-1] > limit:
            q.pop()
            cnt+=1
    else:
        if q[0] <= limit:
            q.pop()
            cnt+=1

print(cnt)