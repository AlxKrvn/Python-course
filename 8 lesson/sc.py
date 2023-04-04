def delete_doubl(s):

    a = []
    for i in range(len(s)):
        for j in s[i + 1:]:
            if s[i] == j:
                a += j
    s -= a            
    return s

list = [input() for i in range(int(input('count = ')))]

print(delete_doubl(list))
