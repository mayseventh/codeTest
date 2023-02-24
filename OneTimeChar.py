def solution(s):
    answer = ''
    check = []

    for i in s:
        if s.count(i) == 1:
            check.append(i)
    
    check.sort()
    answer = ''.join(check)

    return answer

print(solution("abcabcadc"))