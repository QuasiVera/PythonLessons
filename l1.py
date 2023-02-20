# a = 30
# b = 4.5
# e = None
# print(f'{a} + {b} = {a+b}')
# print(e)
# c =int(input('Введите целое число: '))
# # print(f"a {type(a)}")
# # print(f"b {type(b)}")
# print(f"c = {c}")

# # print(f'a + c = {a} + {c} = {a+c}')
# # a = 'abcde'
# # b = "qwerty"

# # print(a+b)
# print(a/c)
# print(a%c)
# # print(f"b {type(b)}")

# name = input("Введите имя: ")
# if name == "Маша" or name == "Пенни":
#     print(f'Ура, это же {name}!')
# elif name == "Шелдон":
#     print('Че почем, ученый?')
# else:
#     print(f"Привет, {name}!")


# n = int(input('Введите число: '))
# k = int(input('Введите номер цифры: '))
# sum = n
# count = 0
# while sum!=0:
#     #sum = sum + n%10
#     sum=sum//10
#     count +=1
# #print("Сумма цифр равна ", sum)
# i=0
# while i<count-k:
#     n=n//10
#     i+=1
# res = n%10
# print(f"{k}-я цифра -> {res}")



# n = int(input('Введите число: '))
# r = range(1,n,1)
# for i in r:
#     print(f'{i}^2 = {i*i}')



# n = int(input('Введите число: '))
# flag = True
# i=2
# while flag:
#     if n % i == 0: # если остаток от деления n на i = 0
#         flag = False
#         print('Делитель', i)
#     elif i > n//2:  # делитель не должен быть больше, чем число, деленное на 2 
#         print(n)
#         flag = False
#     i += 1



text = 'Съешь ещё этих МягкиХ фраНцузских булок'
print(len(text))
print(text.upper())
print(text.lower())
print(text.replace('ещё', 'побольше'))

print()
print(text[-2])  # выводит n-й символ строки с конца, если [-2] то 2-й с конца
print(text[2:9]) # выводит n-й
    






# \t - табуляция, \n - с новой строки,  \' - поставить кавычку как элемент(символ) строки
# ab\tcd = ab  cd, ab\ncd =  (abcd в две строки, см. ниже), ab\'cd = ab'cd
# ab
# cd

