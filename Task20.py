enLetters1 = {'a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r'}
enLetters2 = {'d', 'g'}
enLetters3 = {'b', 'c', 'm', 'p'}
enLetters4 = {'f', 'h', 'v', 'w', 'y'}
enLetters5 = {'k'}
enLetters8 = {'j', 'x'}
enLetters10 = {'q', 'z'}

dictEn = {'8' : enLetters8, '10' : enLetters10, '1': enLetters1, '2': enLetters2, 
          '3' : enLetters3, '4': enLetters4, '5': enLetters5}

str = 'harmony'
score = 0
for k in range(0, len(str)): # идем по строке, перебираем по одной букве
    for i in dictEn:         # идем по словарю по ключам i
        for j in dictEn[i]:  # идем по значениям, j - это одна буква в множестве под индексом i
            if str[k] == j:
                i = int(i)
                print(f'{str[k]} -> {i}')
                #print(type(i))
                score = score + i
print(f'{str} -> {score} очков')

# print(type(dictEn))
# for i in dictEn:
#     for j in dictEn[i]:
#         if 
#         print(j)
