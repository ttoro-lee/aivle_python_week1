# Q5 Answer template
def solution(n, s):
    answer = []
    
    # 9 // 2 = 4
    # 5 // 1 = 5
    
    # 10 // 3 = 3
    # 7 // 2 = 3
    # 4 // 1 = 4
    
    while(s != 0):
        if s//n == 0:
            return [-1]
        answer.append(s//n)
        s = s - (s//n)
        n -= 1
    
    return answer

n = 2
s = 9
answer = solution(n, s)
print(answer)