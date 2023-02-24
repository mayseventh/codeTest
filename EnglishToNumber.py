def solution(numbers):
    answer = 0

    temp = numbers.replace("one", "1")
    temp = temp.replace("two", "2")
    temp = temp.replace("three", "3")
    temp = temp.replace("four", "4")
    temp = temp.replace("five", "5")
    temp = temp.replace("six", "6")
    temp = temp.replace("seven", "7")
    temp = temp.replace("eight", "8")
    temp = temp.replace("nine", "9")
    temp = temp.replace("zero", "0")

    print(temp)
    answer = int(temp)
    return answer

print(solution("onefourzerosixseven"))