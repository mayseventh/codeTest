def solution(spell, dic):
    answer = 0
    
    check = 0
    
    for i in dic:
        for j in spell:
            if i.find(j) >= 0:
                check += 1
        
        if check == len(spell):
            print(i)
            answer = 1
            break
        else:
            answer = 2
            check = 0
    
    return answer

print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))
print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))