import math
def solution(n):
    answer = 0
    lcm = (n*6)//math.gcd(n, 6)

    answer = lcm//6

    return answer

print(solution(10))