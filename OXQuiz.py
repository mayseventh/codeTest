def solution(quiz):
    answer = []

    for i in quiz:
        l_quiz = i.split(" ")
        print(l_quiz)

        sol = int(l_quiz[0])

        for j in range(1, len(l_quiz)):
            if l_quiz[j] == "+":
                sol += int(l_quiz[j+1])
            elif l_quiz[j] == "-":
                sol -= int(l_quiz[j+1])
            elif l_quiz[j] == "=":
                print("sol, l_quiz[j+1] : {0}, {1}".format(sol, l_quiz[j+1]))
                if sol == int(l_quiz[j+1]):
                    answer.append("O")
                else:
                    print("here")
                    answer.append("X")

    return answer

print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))