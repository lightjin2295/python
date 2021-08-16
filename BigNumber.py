number = "4177252841"
numList = [int(i) for i in number]
k = 4

stack = []

for i in number:

    while stack and i > stack[-1]:

        if k > 0 :
            print(i)
            print(stack)
            stack.pop()
            k-= 1
        else :
            break

    stack.append(i)
    print(11111111)
    print(stack)

if k > 0:
    for _ in range(k):
        stack.pop()


answer = "".join(stack)
print(answer)



