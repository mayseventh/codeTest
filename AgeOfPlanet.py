def solution(age):
    answer = ''
    planet_age = {0:"a", 1:"b", 2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j"}
    
    for i in str(age):
        print("i, age, age[i] : {0}, {1}, {2}".format(i, age, planet_age[int(i)]))
        answer += planet_age[int(i)]
    return answer

print(solution(23))