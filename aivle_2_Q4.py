# Q4 Answer Template

def solution(arr):
    while(len(arr) > 1):
        a = arr.pop()
        b = arr.pop()
        tmp = gcd(a,b)
        lcm = (a * b) // tmp
        arr.append(lcm)
    return arr[0]

def gcd(a, b):

    while(b>0):
        a, b = b, a%b
    return a

arr = [None]*15
arr = [2,6,8,14]
answer = solution(arr)
print(answer)