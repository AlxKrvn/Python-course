def delete_doubl(s):

    for i in s:
        while s.count(i) > 1:
            del s[s.index(i)]
    return s

list = [input() for i in range(int(input('count = ')))]

print(delete_doubl(list))