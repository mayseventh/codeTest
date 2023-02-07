def solution(letter):
    answer = ''
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    
    temp = letter.split()
    print(temp)

    for i in temp:
        if i != ' ':
            answer += morse[i]
    return answer

print(solution(".... . .-.. .-.. ---"))
print(solution(".--. -.-- - .... --- -."))