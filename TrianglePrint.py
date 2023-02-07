n = int(input())
print(n)

for i in range (1, n+1):
    star = ""
    for j in range (1, i+1):
        star += "*"
    print(star)

