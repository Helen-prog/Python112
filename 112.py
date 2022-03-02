# first_name = "Elena"
# print("Hello,", first_name)
# age = 20
# print(age)
# print(id(age))
# print(type(age))
# age = "Hi"
# print(type(age))
# age = 2.89  # Вещественное число
# print(type(age))  # вывод

# a = b = c = 1
# print(a, b, c)

# a, b, c = 5, "Hello", 9.2
# print(a, b, c)

# let a=5, b="Hello";


# PI = 3.14
# print(PI)

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# c = a
# a = b
# b = c
# print("a:", a)
# print("b:", b)

# print("\tДокумент '112.py' находится по заданному пути \"D:\\Python112\\112.py\"Документ '112.py' находится по "
#       "заданному пути \"D:\\Python112\\112.py\"")


# s1 = "Hello"
# s2 = "world"
# s3 = s1 + " " + s2 + "!\t\t"
# print(s3)
# print(s3 * 5)
# print("5 " * 10)

# print(-5.964654564564548967487897896748967478978979879879)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)
# print(7 / 2)
# print(7 // 2)
# print(7 ** 2)
# print(7 % 2)
#          3    2   1   4
# number = 6 + 4 * 5 ** 2 + 7
# print(number)
#
# number1 = (6 + 4) * (5 ** 2 + 7)
# print(number1)

# num = 10
# num += 5  # num = num + 5
# num += 1
# num -= 1
# num *= 2
# print(num)
# num = 1234
# a = num % 10
# print(a)
# num = num // 10
# print(num)
# b = num % 10
# print(b)
# num = num // 10
# # print(num)
# c = num % 10
# print(c)
# num = num // 10
# # print(num)
# d = num % 10
# print(d)
# print(a, b, c, d)

# num = 1234
# res = (num % 10) * 1000  # 4000
# num = num // 10
# res += (num % 10) * 100  # 300
# num = num // 10
# res += (num % 10) * 10  # 20
# num = num // 10
# res += num % 10  # 1
# print(res)

# int() - преобразовывает значение к целому числу
# str() - преобразование к строковому типу
# float() - преобразование к вещественному типу данных
# num1 = "2.8"
# num2 = 3
# # res = int(num1) + num2
# res = float(num1) + num2
# print(res)

# print(int(3.8))
# print(round(3.891))
# print(round(3.895, 2))
# a = 5 / 3
# print(a)
# print(round(a, 2))

# name = "Виктор"
# age = 28
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="--", end="\n\n")
# print("Я учу Python", end="____")
# print("Я учу Python")

# name = "Igor"  # %s
# age = 26  # %d
# grade = 9.2  # %f
# print("It's %s, %d. Level: %.1f" % (name, age, grade))
#
# print("{2} This is a {1}. It's {0}.".format(10, "hello", 60))

# num = int(input("Ваше имя: "))
# b = input("Ваш город: ")
# print(5 + num)

# b1 = True
# b2 = False
# print(b1 + 5)
# print(b2 + 5)
#
# print(type(b1))
# print(bool("python"))
# print(bool(""))  # False
# print(bool(" "))
# print(bool(-5))
# print(bool(10))
# print(bool(0))  # False
# print(bool(0.1))
# print(bool(False))  # False
# print(bool(None))  # False

# test = None
# print(test)
# print(test is None)
# test = 5
# print(test)
# print(test is None)

# print(7 == 7)
# print(2 + 5 == 7)
# print(7 != 10-3)
# print("привет" > "ПРИВЕТ")

# print(2 < 4 < 9)
# print(2 * 5 > 7 >= 4 + 3)
# print(3 * 3 <= 7 >= 2)
#
# a = 10
# b = 5
# c = a == b
# print(a, b, c)


# print(5 - 3 == 2 or 1 + 3 == 4)
# print(5 - 3 == 2 or 1 + 3 < 4)
# print(5 - 3 > 2 or 1 + 3 == 4)
# print(5 - 3 > 2 or 1 + 3 < 4)

# print(not 9 - 5)
# print(not 9 - 9)
#
# cnt = 5
# if cnt < 10:
#     cnt += 1
# print(cnt)

# let cnt = 15;
# if(cnt<15){
#     cnt++;
# }
# console.log(cnt);

# age = int(input("Введите свой возраст: "))
# if age >= 18:  # 23 > 18
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# PEP8

# a = 15
# b = 5
# if a > b:
#     print("a > b")
# if b > a:
#     print("b > a")
# if a == b:
#     print("a == b")
# a = 15
# b = 15
# if a > b:
#     print("a > b")
# elif b > a:  #else if
#     print("b > a")
# else:
#     print("a == b")

# a = int(input("-> "))
# b = int(input("-> "))
# c = int(input("-> "))
#
# if a == b == c:
#     print("равносторонний")
# elif a == b or b == c or c == a:
#     print("равнобедренный")
# else:
#     print("разносторонний")


# day = int(input("Введите день недели (цифрой): "))
# if (day >= 1) and (day <= 5):
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")

#
# m = int(input("Введите номер месяца"))
# if 1 <= m <= 12:  # (m >= 1) and (m <= 12)
#     if m == 1 or m == 2 or m == 12:
#         print("Зима")
#
# else:
#     print("Ошибка данных")

# a = int(input("->"))
#
# if a > 0 and a <= 3:
#     print("зима")
# elif a > 3 and a <= 6:
#     print("Весна")
# elif a > 6 and a <= 9:
#     print("лето")
# elif a > 9 and a <= 12:
#     print("осень")
# else:
#     print("неверное значение")

# a = int(input("Введите число от 1 до 99: "))
# kop = a
# if 11 <= kop <= 14:
#     print(a, "копеек")
# else:
#     kop = kop % 10
#     # kop = a % 10
#     if kop == 1:
#         print(a, "копейка")
#     elif 2 <= kop <= 4:
#         print(a, "копейки")
#     else:
#         print(a, "копеек")

# (Условие) ? TRUE : FALSE - JS

# TRUE if (уловие) else FALSE  - тернарное выражение
# a, b = 30, 20
# minim = a if a < b else b
# print(minim)
# a, b = 30, 0
# print("a == b" if a == b else ("a > b" if a > b else "b > a"))

# a = 5
# b = 0
# print(a / b)
# try except
# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")
# print("Код дальше")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
#     print("Все вывелось!")
# except (ValueError, ZeroDivisionError):
#     print("Значение должно быть челым числом")
#     print("Нельзя делить на ноль")
# else:
#     print("Все нормально, вы ввели числа", n, "и", m)
# finally:
#     print("Конец программы")
# n = int(input("Введите первое число: "))
# m = int(input("Введите второе число: "))

# a = int(input("Первое число --->"))
# b = int(input("Второе число --->"))
# try:
#
#     c = a + b
#     print(c)
# except ValueError:
#     print("Вы написали не число")
#     print(str(a + b)

# n = input('Введите первое значение ')
# m = input('Введите второе значение ')
# try:
#     n = int(n)
#     m = int(m)
# except (TypeError, ValueError):
#     n = str(n)
#     # m = str(m)
# finally:
#     print(n + m)

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1  # i = i - 1

# i = 2
# while i < 21:
#     print("i =", i)
#     i += 2


# i = 13
# while i < 20:
#     i += 1
#     if i % 2 == 0:
#         print(i)

# n = int(input("Укажите количество символов: "))
# while n > 0:
#     print("*")
#     n -= 1


# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# z = int(input("Input namber of star "))
# print(z * '*')
# x = 12
# y = '*'
# s = ' '
# while x <= 18:
#     print(y)
#     s = s + y
#     print(s)
#     x = x + 1
# print(s)

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# s = 0
# while a <= b:
#     if a % 2 != 0:
#         s += a
#     a += 1
# print(s)

# a = int(input("Первое число --->"))
# b = int(input("Первое число --->"))
#
# i = a
# c = 0
# while i <= b:
#     if i % 2 != 0:
#
#         c = c + i
#     i += 1
# print(c)

# a = int(input("Введите число: "))
# b = 0
# c = 0
# ans = a
# while a > 0:
#     b = a % 10
#     c = c * 10 + b
#     a = a // 10
#
# # if c == ans:
# #     print("Число " + str(ans) + " - палиндром")
# # else:
# #     print("Число " + str(ans) + " - не палиндром")
#
# print("Число", ans, ("-" if c == ans else "- не"), "палиндром")

# kol = int(input("Введите количество чилел последовательности: "))
# i = 1
# ch = float(input("Введите число: "))
# min_ch = ch
# max_ch = ch
# sum_ch = ch
# while i < kol:
#     ch = float(input("Введите число: "))
#     sum_ch += ch  # sum_ch = sum_ch + ch
#     if ch < min_ch:
#         min_ch = ch
#     if ch > max_ch:
#         max_ch = ch
#     i += 1
# averange = sum_ch / kol
#
# print("Минимальное число:", min_ch)
# print("Максимальное число:", max_ch)
# print("Среднее арифметическое:", averange)

# n = input("Введите целое число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while True:
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен!")


# while True:
#     n = int(input("Введите положительное число: "))
#     if not n > 0:  # if n < 0
#         break

# i = 0
# while i < 10:
#     # if i == 5:
#     #     break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)
#
# print("За пределами цикла")

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i*j)
#         j += 1
#
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end='\t\t')
#         j += 1
#     print()
#     i += 1
# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     print(" " * i, "*")
#     i += 1
#
# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1

# for i in "Hello!":
#     print(i)
# i = 1
# for color in 'red', 'green', 'yellow', 1, 20, 0.3:
#     print(i, "color:", color)
#     i += 1
# print(range(9))

# for(let i = 0; i < 12; i++){}

# range(start, stop, step)

# for i in range(0, 12, 2):
#     print(i, end=" ")
# print()
# for i in range(0, 12, 2):
#     print(i, end=" ")
# print()
# for i in range(2, 9, 3):
#     print(i, end=" ")
# print()
# for i in range(100, 0, -10):
#     print(i, end=" ")

# a = int(input("Введете целое число: "))
# for i in range(1, a):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('done')

# w = int(input("width: "))
# h = int(input("height: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# for i in range(10):
#     if i % 2 == 0:
#         print(i, end=" ")
#
# print()
#
# print([i for i in range(10) if i % 2 == 0])
#
# print([letter * 2 for letter in "Banana"])

# nums = [8, 3, 6, 9, 7, 3]
# print(nums)
# print(type(nums))
#
# print(type([2, 3.2, "three", True]))

# nums = [8, 3, 6, 9, 7, 4]
# print(nums[0])
# print(nums[1])
# print(nums[5])
# print(nums[-1])
# nums[-1] = 253
# print(nums)
# nums[3] += 100
# print(nums)
# print("Длина списка:", len(nums))

# a = [1, 2]
# print(id(a))
# a[1] = 3
# print(a)
# print(id(a))

# s = list("Hello")
#
# print(s)

# n = [5, 1] * 6
# print(n)
# n2 = [10, 8, 6, 4]
# print(id(n2))
# n = list(range(10, 2, -2))
# print(id(n))
# print(n2)
# print(n)
#
# if n == n2:
#     print("Списка равны")
# else:
#     print("Списки разные")
#
# if n is n2:
#     print("Списка равны")
# else:
#     print("Списки разные")
# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)
#
# a = [1, 2, 3]
# b = [4, 5]
# a += b  # [1, 2, 3, 4, 5]
# c = a + b
# print(c)
# print(c * 3)

# a = [0] * int(input("Введете количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# print(id(a))
# print("*" * 20)
# # for i in range(len(a)):
# #     a[i] += 5
# #     print(a)
# print("*" * 20)
#
# print([a[i] + 5 for i in range(len(a))])
# print(id(a))

# a = list(range(10, 100, 10))
# print(a)
# for i in range(len(a)):
#     print(a[i] + 2, end=" ")
# print()
# for i in a:
#     print(i + 2, end=" ")


# a = list(range(21, 41))
# s = d1 = 0
# # d = 0
# # s1 = 0
# print(a)
# print('*-' * 20)
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         s += 1
#         # s1 += a[i]
#     else:  # if a[i] % 2 != 0:
#         # d += 1
#         d1 += a[i]
# print(s)
# # print(d)
# # print(s1)
# print(d1)

# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# s = k = 0
# for i in range(len(a)):
#     s += a[i]
#     if a[i] != 0:
#         k += 1
# print("Среднее арифметическое:", s / k)


#  список[start:stop:step]

# s = [5, 9, 3, 7, 1, 8]
# print(s[10:1:-1])

# s = list(range(1, 8))  # [1, 2, 3, 4, 5, 6, 7]
# print(s[1:-2])
# print(s[-2:1:-1])
# print(s[:])
# print(s[::-1])  # [7, 6, 5, 4, 3, 2, 1]
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4])
# print(s[4:])
# print(s[4:1:-1])
# print(s[-3:1:-1])
# print(s[2:5])


# lst = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(lst)
# for j in range(len(lst)):
#     for i in range(len(lst)):
#         if lst[j] == lst[i] and j != i:
#             break
#     else:
#         print(lst[j], end=" ")

# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s[1:3])  # [3, 5]
# s[1:3] = [20, 2]
# print(s)
# s[4] = [30]
# print(s)
#
# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# last = s.pop()
# print(last)
# print(s.pop(0))  # удаляет по индексу
# s[2:7] = []
# s.remove(2)  # удаляется первое заданное значение
# s.clear()
# del s[2:6]
# print(s)
# s.append(99)
# print(s)
# s.extend([11, 77, 66])
# print(s)
# s.insert(2, 100)
# print(s)

# lst = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#     lst.append(x)
# print(lst)

# d = []
# n = int(input('Введите количество циклов: '))
# for i in range(n):
#     x = int(input('Введите число: '))
#     if x % 3 == 0:
#         d.append(x)
#     else:
#         print('Число', x, 'не кратно 3. Пожалуйста, введите число, кратное 3')
# print(d)

# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
# print(c)  # [2, 1, 4, 3]

# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# for i in range(len(b)):
#     c.append(a[i])
#     c.append(b[i])
# print(c)

# print("Введите элемены списка:")
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# print("Введите индекс:")
# k = int(input("k = "))
# a.pop(k)
# print(a)

# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# num = s.count(2)
# print(s)
# ind = s.index(2, 5, -1)
# print(ind)
# s_copy = s.copy()
# print(s_copy)
# s.append(120)
# print(s)
# print(s_copy)
# print(id(s))
# print(id(s_copy))
#
# a = [1, 2, 3]
# b = a
# print("a =", a)
# print("b =", b)
# b.append(20)
# print("a =", a)
# print("b =", b)
# print(id(a))
# print(id(b))
# s.reverse()
# print(s)
# s.sort()  # reverse=False
# print(s)

# print(s.sort(reverse=True))
# print(sorted(s, reverse=True))
# print(s)

# s2 = ["Виталий", "Сергей", "Александр", "Анна"]
# s2.sort(key=len, reverse=True)
# print(s2)


# print("Введите элементы списка: ")
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# print("Введите число для удаления: ")
# k = int(input("k = "))
# # a.remove(k)
# # print(sorted(a, reverse=True))
# ind = a.index(k)
# a.pop(ind)
# a.sort(reverse=True)
# print(a)
# from random import choices
# import random as r

# from random import randint, randrange

# print(random.random())  # от 0 до 1

# print(r.randint(1, 9))  # 9 включительно
# print(randrange(2, 9, 2))

# city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# print(r.choice(city_list))
#
# s = [55, 66, 77, 88, 99]
# print(r.choice(s))
#
# s3 = [20, 30, 40, 50, 60, 70, 80, 90]
# print(choices(s3, k=5))
# r.shuffle(s3)
# print(s3)

# print(r.uniform(10.5, 25.5))
# print(round(r.uniform(10.5, 25.5), 2))

# mas = [i for i in range(10)]
# print(mas)
#
# mas1 = [r.randint(1, 100) for i in range(10)]
# print(mas1)

# lst = [5, 3, 2, 4, 1]
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))

# sum = [5, 3, 2, 4, 1]
# print(min(sum))
# print(sum(sum))
# mas1 = [r.randint(1, 100) for i in range(10)]


# from random import randint  # Задание произвольного массива
#
# n = [randint(1, 50) for i in range(10)]
# print(n)
# m = max(n)
# print(m)
# # for i in n:
# #     if i == m:
#
# n.remove(m)
# print(n)
# n.insert(0, m)
# print(n)

# from random import randint  # Задание произвольного массива
#
# n = [randint(0, 100) for i in range(10)]
# print(n)
# c = min(n)   # min
# print(c)
# s = n.index(c)  # index
# print(s)
# # del n[0:s]
# print(n[s:])

# x = list('1a2b3')
# print(x)
# print('a' in x)
# print('e' in x)
# print()
# print('a' not in x)
# print('e' not in x)

# lst = []
# if len(lst) == 0:
#     print("Список пустой")
#
# if not lst:
#     print("Список пустой")
# else:
#     print("В списке есть элементы")

# n1 = 5
# n2 = 4
# a = [r.randint(0, 10) for i in range(n1)]
# b = [r.randint(0, 10) for j in range(n2)]
# print("Первый список:", a)
# print("Второй список:", b)
# c1 = a + b
# print("Третий список:", c1)
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Элементы обоих списков без повторений:", c)
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Элементы общие для двух списков:", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print("Минимальное и максимальное для каждого из списков:", c)

# m = [
#     [1, 2, 3, 4, 7, 9],
#     [5, 6, 7, 8, 2],
#     [9, 10, 11, 12],
#     [1]
# ]
# print(m)
# print(m[1][2])  # 7
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()
# print()
# for row in m:
#     for col in row:
#         print(col, end="\t\t")
#     print()

# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# for row in matrix:
#     for col in row:
#         print(col, end="\t\t")
#     print()
# print()
# squared = [[col ** 2 for col in row] for row in matrix]
# for row in squared:
#     for col in row:
#         print(col, end="\t\t")
#     print()

# 0  0  0  0  0
# 0  0  0  0  0
# 0  0  0  0  0
# w, h = 5, 3
# squared = [[0 for col in range(w)] for row in range(h)]
# for row in squared:
#     for col in row:
#         print(col, end="\t\t")
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)


# mas = [
#     [2, 5, 8],
#     [5, 8, 2],
#     [8, 7, 1],
#     [0, 7, 1],
#     [9, 11, 6]
# ]
# print(mas)
# for row in mas:
#     for x in row:
#         print(x, end="\t")
#     print()
# print()
#
# for i in range(len(mas)):
#     if i % 2 == 0:
#         mas[i].sort(reverse=True)
#     else:
#         mas[i].sort()
#
# for row in mas:
#     for col in row:
#         print(col, end="\t")
#     print()

# a = [r.randint(1, 10) for i in range(10) if i not in a]
# ============================
# b = int(input("Размер списка: "))
# a = list()
# # for i in range(50):
# while len(a) != b:  # 10
#     w = r.randint(1, b)  # 9
#     if w not in a:
#         a.extend([w])  #
# print(a)
# ============================
# lst = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# row = 0
# for row in lst:
#     for col in row:
#         print(col, end="\t")
#     print()
# print("-------")
# i = 0
# for col in row:
#     for row in lst:
#         print(row[i], end="\t")
#     i += 1
#     print()
# ============================

# w, h = 10, 3
# matrix = [[r.randint(1, 30) for x in range(w)] for y in range(h)]
# matrix = []
# for y in range(h):
#     m = []
#     for x in range(w):
#         m.append(r.randint(1, 30))
#     matrix.extend([m])

# print(matrix)
# for h in matrix:
#     for w in h:
#         print(w, end="\t\t")
#     print()
#
#
# w, h = 3, 4
# matfor h in matrix:
#     for w in h:
#         print(w, end="\t\t")
#     print()rix = [[r.randint(1, 30) for x in range(w)] for y in range(h)]


# from random import randint  # Задание произвольного массива
#
# w, h = 6, 6
# matrix = [[randint(0, 10) for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for col in row:
#         print(col, end='\t\t')
#     print()
# print()
# for h in range(len(matrix)):
#     if h % 2 == 0:
#         for w in range(len(matrix[h])):
#             print(matrix[h + 1][w], end="\t\t")
#         print()
#         for w in range(len(matrix[h])):
#             print(matrix[h][w], end="\t\t")
#         print()

# for row in range(len(matrix)):
#     if row % 2 == 0:
#         row = matrix[row + 1]
#     else:
#         row = matrix[row - 1]
#     for col in row:
#         print(col, end="\t\t")
#     print()


# 1  2  3  4  5
# 8  9  10 11 12
# 15 16 17 18 19
# 22 23 24 25 26
# 29 30 31

# days = [d for d in range(1, 32)]
# print(days)
# print(len(days))
# weeks = [days[i:i+5] for i in range(0, len(days), 7)]
# print(weeks)
# for row in weeks:
#     for x in row:
#         print(x, end="\t\t")
#     print()

# import math
#
# print(math.sqrt(2))
# print(math.floor(3.8))
# print(math.ceil(3.2))
#
# import math as m
#
# print(m.sqrt(2))
# print(m.floor(3.8))
# print(m.ceil(3.2))

# from math import *

# print(sqrt(2))
# print(floor(3.8))
# print(ceil(3.2))
# print(pi)
#
#
# r = int(input("Радиус"))
# print(2 * pi * r)
#
# c = int(input('Введите радиус окружности: '))
#
# print("Радиус окружности равен:", round(2 * pi * c, 2))

# lst = [1, 5, 3, 8.4]
# print(sum(lst))
# print(fsum(lst))
#
# print(degrees(3.14159))  # перевод из радиан в градусы
# print(radians(180))  # перевод из градусов в радианы
#
# print(cos(radians(60)))
# print(sin(radians(60)))

# a = int(input("a = "))
# b = int(input("b = "))
# print('Гипотенуза равна: ', sqrt((a**2)+(b**2)))


# import random
#
# n = int(input('Размерность массива: '))
# mas = [[random.randint(0, 10) for x in range(n)] for y in range(n)]
# print('Массив из случайный чисел от 1 до 100:')
# for row in mas:
#     for x in row:
#         print(x, end='\t')
#     print()
# print()
# m = 100
# for k in range(n):
#     if m > mas[k][k]:
#         m = mas[k][k]
# print('Минимальный элемент массива: ', m)

# seconds = time.time()
# print(seconds)
# local_time = time.ctime(seconds)
# print(local_time)
# res = time.localtime()
# print(res)
# print(res.tm_hour)
#
# print(time.strftime("Today is %B %d, %Y", time.localtime()))
# print(time.strftime("%m/%d/%Y, %H:%M:%S"))

# pause = 0.5
# print("Program started...")
# time.sleep(pause)
# print(pause, "seconds.")

# text = input("Название напоминания: ")
# t = float(input("Через сколько минут: "))
# t *= 60
# time.sleep(t)
# print(text)

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# result = finish - start
# print(result)

# import locale

# locale.setlocale(locale.LC_ALL, "ru")
#
# print(time.strftime("Сегодня: %B %d, %Y", time.localtime()))

# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")

# функции


# def hello(name, word):  # аргументы
#     print("Hello, ", name, ". Say ", word, sep="")
#
#
# hello("Irina", "hi")  # параметры
# hello("Ivan", "hello")


# def get_sum(a, b):
#     print(a + b)
#
#
# n = 2
# m = 5
# get_sum(n, m)
# x = 1
# y = 8
# get_sum(x, y)
# get_sum("abc", "def")


# def symbol():
#     pass
# def symbol(x, y, z):
#     s = ''
#     for i in range(x):  # от 0 до 9
#         if i % 2 == 0:
#             s += y
#         else:
#             s += z
#     print(s)

# def symbol(num, s1, s2):
#     for ch in range(num):
#         if ch % 2 == 0:
#             print(s1, end='')
#         else:
#             print(s2, end='')
#     print()


# symbol(9, "+", "-")
# symbol(7, "X", "0")


# def get_sum(a, b):
#     print("Строка")
#     return a + b
#
#
# n = 2
# m = 5
# res = get_sum(n, m)
# print(res)


# def maximum(one, two):
#     if one > two:
#         return one
#     elif two > one:
#         return two
#     else:
#         return
#
#
# m = maximum(9, 9)
# print(m)

# def add(x, y):
#     if x > y:
#         return x - y
#     elif x < y:
#         return x + y
#
#
# a = int(input("a = "))
# b = int(input("b = "))
# m = add(a, b)
# print(m)


# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# Ряд Фибоначчи
# 0 1 1 2 3 5 8 13

# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=" ")
#         # a, b = b, a + b
#         c = a + b
#         a = b
#         b = c
#
#
# fib(15)

# def change(lst):
#     pass

# def change(s):
#     a = s[0]
#     b = s[-1]
#     for i in range(len(s)):
#         if i == 0:
#             s[i] = b
#         if i == len(s) - 1:
#             s[i] = a
#         print(s[i], end=' ')

# def change(s):
#     s[0], s[-1] = s[-1], s[0]
#     return s

# def change(lst):
#     start = lst.pop()  # 3
#     end = lst.pop(0)  # 1
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(is_greater(10, 5))
# print(is_greater(5, 10))

# def chech_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return password
#     return
#
#
# p = input("Введите пароль: ")  # 125An456
# if chech_password(p):
#     print("Это надежный пароль.")
# else:
#     print("Это не надежный пароль.")

# def get_sum(a=5, b=3, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(d=2))

# def set_param():
# def set_param(x=20, y='-'):
#     print(x * y)
#
#
# set_param(10, "+")
# set_param(5, "*")
# set_param(15, "#")
# set_param(7)
# set_param()

# def check_password(username, password, min_length=8, check_user=True):
#     if len(password) < min_length:
#         print("Пароль слишком короткий")
#         return False
#     elif check_user and username in password:
#         print("Пароль содержит имя пользователя")
#         return False
#     else:
#         print("Пароль для пользователя", username, "прошел все проверки")
#         # return True
#
#
# check_password('igor', '12345')
# check_password('igor', '12456igor')
# check_password('igor', '12345name')

# def digit_sum(username):
#
#     username = str(username)
#     sum = 0
#     sum1 = 0
#     for i in username:
#         c = int(i)
#         if c % 2 == 0:
#             sum += c
#         else:
#             sum1 += c
#     print('Сумма четных элементов: ', sum)
#     print('Сумма нечетных элементов: ', sum1)
# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр: ")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print("Сумма нечетных цифр: ")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age, "\n")
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")

# def func(a, ln=None):
#     if ln is None:
#         ln = []
#     ln.append(a)
#     return ln
#
#
# print(func(1, ln=[2, 3]))
# print(func(2))  # [1, 2]
# print(func(3))  # [1, 2, 3]

# a = 5
# b = 5
# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)
#
# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
#
# print(lt1 == lt2)
# print(lt1 is lt2)

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1 = [4, 5]
# # lt1.append(4)
# # lt1.pop(1)
# # lt1[1] = "Hello"
# print(lt1)
# print(id(lt1))

# s = "Hello"
# s1 = "Hello"
# # print(id(s))
# # s = s[1:-1]  # ell
# # print(s)
# print(id(s))
# print(id(s1))
# print(s == s1)
# print(s is s1)

# a = 5
# print(id(a))
# a += 1  # a = a + 1
# print(a)
# print(id(a))

# def add_number(n):
#     print("Внутри функции:", n, "=", id(n))
#     n = n + [4]  # n += [4]
#     print("После присвоения:", n, "=", id(n))
#
#
# x = [1, 2, 3]
# print(x, "=", id(x))
# add_number(x)
# print(x, "=", id(x))


# Кортеж (tuple)
# lst = [10, 20, 30]
# tp = (10, 20, 30)
# print(lst.__sizeof__())
# print(tp.__sizeof__())


# a = (1, 2, 3, 4, 5)
# print(a)
# print(type(a))
# b = 1, 2, 3
# print(tuple(b))
# print(type(b))

# t = tuple('hello')
# print(t)
# print(type(t))

# a = tuple((1, 2, 3, 4, 5))
# print(a)
#
# print(a[1:3])
# print(a[3])
# a[3] = 7
# print(a)

# s1 = tuple(int(input("-> ")) for i in range(1, 3))
# print(s1)

# import random
#
# s1 = tuple(random.randint(0, 100) for i in range(10))
#
# print(s1)

# cp = tuple(2 ** i for i in range(13))
# print(cp)

# t1 = tuple("hello")
# t2 = tuple(" world")
# t3 = t1 + t2
# print(t3)
# print(len(t3))
# print(t3.count('l'))
# print(t3.count('a'))
# print(t3.index('l'))


# if 'l' in t3:
#     print(t3.index('l'))
# else:
#     print("Такого символа нет")

# for i in t3:
#     if i == " ":
#         continue
#     print(i, end=" ")

# t = (10, 11, [1, 2, 3], [4, 5, 6], ["hello", "world"])
# print(t, id(t))
# t[4][0] = "new"
# t[4].append('hi')
# print(t, id(t))

# def func(ls):
#     pass
#     return tuple()
#
#
# print(func([1, 2, 3, 3, 2]))
# print(func([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))
# from random import randint
#
# x = [randint(0, 9) for i in range(10)]
# print(x)
#
#
# def func(s):
#     ls = []
#     [ls.append(i) for i in reversed(s) if i not in ls]
#     # for i in s:
#     #     if i not in ls:
#     #         ls.append(i)
#     # print(ls)
#     return tuple(ls)
#
#
# print(func(x))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа
# print(x, y, z)
#
#
# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)
# n, a, i = user
# print(n, a, i)

# t = (1, 2, 3)
# del t
# print(t)

# lst = (1, 2, 3, 4, 5)
# print(type(lst))
# print(lst)
# tp = list(lst)
# print(type(tp))
# print(tp)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))), ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана:", country_name, "население =", country_population)
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород:", city_name, "население =", city_population)

# s = {1, 2, 1, 2, 3, 2, 3, 8}
# print(type(s))
# print(s)
# print(len(s))

#  Множества (set)
# c = ["hello", "hi", 'hi']
# a = set(c)
# b = {"hello", "hi", 'hi'}
# print(b)


# s = {x for x in range(10) if x % 2 == 0 if x > 5}
# print(s)
# s = tuple(s)
# print(s)
# print(set(s))

# numbers = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# print(list(set(numbers)))

# def to_set(element):
#     pass
# def to_set(x):
#     a = set(x)
#     return a, len(a)
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))
#

# t = {"red", "green", "blue"}
# # print("green" not in t)
# for i in t:
#     print(i, end=" ")

# [res for()]
# [res for() if]
# [res if() else for()]
# [res if() else for() if]

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {'A' + i[1:] if i[0] == 'a' else "B" + i[1:] for i in r if i[1] == "c"}
# print(a)

# a = {"0", "1", "2", "3"}
#
# # a.add(4)
# print(a)
# # num = 2
# # if num in a:
# #     a.remove(num)
#
# # a.discard(6)
# # a.pop()
# a.clear()
# print(a)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# # c = a.union(b)
# # a |= b
# # c = a - b
# # c = a.copy()
# # b <= a
# # a.issubset(b)
# print(b < a)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# res1 = s1 ^ s2 ^ s3 ^ s4 ^ s5 ^ s5 ^ s7
# print(res1)
# res2 = max(res1)
# res3 = min(res1)
# print(res2)
# print(res3)

# s1 = "Hello"
# s2 = "How are you"
# a = set(s1) & set(s2)
# for i in a:
#     print(i, end=" ")


# frozenset - вид множества, которое не может быть изменено.

# s = frozenset([1, 2, 3, 4, 5])
# print(s)
# a = frozenset({"hello", "world"})
# print(a)
# b = frozenset({i ** 2 % 4 for i in range(10)})
# print(len(b))

#  dict (Словарь)
# ls = ["один", "два"]
# print(ls[0])
# d = {"one": "один", "two": "два", 1: True}
# print(d["one"])
# print(d)
# print(type(d))

# d = {1: "один", "two": "два"}
# print(d)
# print(type(d))
#
# d1 = dict(a1="один", two="два")
# print(d1)
# print(type(d1))

# d3 = dict.fromkeys(['a', 'b'], 100)
# print(d3)

# users = (
#     ('igor@gmail.com', "Igor"),
#     ('irina@gmail.com', "Irina"),
#     ('anna@gmail.com', "Anna")
# )
# users = (("a", "b"),)
#
# print(users)
# d_users = dict(users)
# print(d_users)

# d4 = {i: i ** 2 for i in range(1, 7)}
# print(d4)
# print(d4[5])
# d4[5] = 50 * 2
# print(d4)

# d5 = {0: "text1", "one": 45, (1, 2, 3): 'кортеж', 42: [2, 3, 6, 7], True: 1}
# key = "one"
# # if key in d5:
# #     del d5[key]
# try:
#     del d5[key]
# except KeyError:
#     print("Элемента с ключем", key, "нет в словаре")
# print(d5)
# del d5[1, 2, 3]
# print("one" in d5)
# print("two" in d5)

# if 'one' in d5:
#     print("TRUE")
# if 'one' in d5.keys():
#     print("TRUE")

# d6 = {'one': 1, 'two': 2, 'three': 3}
# for key in d6:
#     print(key, "->", d6[key])

# x = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# s = 1
# for key in x:
#     s *= x[key]  # s = s * x[key]
# print(s)

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# print(d)

# d6 = {'one': 1, 'two': 2, 'three': 3}
# print(len(d6))

# capitals = dict()
# capitals['Россия'] = "Москва"
# capitals['Италия'] = "Рим"
# capitals['Испания'] = "Мадрид"
#
# countries = ['Россия', 'Италия', 'Франция', 'Испания']
#
# for country in countries:
#     if country in capitals:
#         print("Столица страны ", country, ": ", capitals[country])
#     else:
#         print("В базе нет страны с названием " + country)

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 6400]
# }
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input("№: ")
#     if n != "0":
#         q = int(input("Количество: "))
#         goods[n][1] = q
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")


# d = {"A": 1, "B": 2, "C": 3}
# x = iter(d)
# print(x)
# print(list(x))
# d.clear()  # {}
# d2 = d.copy()
# # d2 = d
# print("D =", d)
# print("D2 =", d2)
#
# d2["B"] = 5
# d["E"] = 7
#
# print("D =", d)
# print("D2 =", d2)

# d = {"A": 1, "B": 2, "C": 3}
# value = d.get("E", "FF")
# print(value)
# print(d)
# new = d.items()
# print(new)
# new1 = dict.items(d)
# print(new1)

# a = d.keys()
# print(a)

# d = {"A": 1, "B": 2, "C": 3}
# # item = d.pop("B", 10)
# # item = d.popitem()
# item = d.setdefault("R", 5)
# print(item)
# print(d)

# d = {"A": 1, "B": 2, "C": 3}
# d.update([("A", 7), ('B', 9)])
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# c = {'b': 5}
# # z = x.copy()
# # z.update(y)  #{'a': 1, 'b': 3, 'c': 4}
# z = x | y | c
# print(z)

# d = {"A": 1, "B": 2, "C": 3}
# v = d.values()
# print(list(v))


# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'NewYork'}
# # a = dict()
# # a['name'] = d.pop('name')
# # a['salary'] = d.pop('salary')
# # print(d)
# # print(a)
# d['location'] = d.pop('city')
# print(d)


# a = {
#     "first": {
#         1: "one",
#         2: "two",
#         3: "three"
#     },
#     "second": {
#         4: "four",
#         5: "five"
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print("\t", y, ": ", a[x][y], sep="")

# sales = {
#     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}
# }
# print(sales)
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t", y, ": ", sales[x][y], sep="")
# from random import randint
#
# a = dict(John=dict(N=randint(1000, 5000), S=randint(1000, 5000), E=randint(1000, 5000), W=randint(1000, 5000)),
#          Tom=dict(N=randint(1000, 5000), S=randint(1000, 5000), E=randint(1000, 5000), W=randint(1000, 5000)),
#          Anna=dict(N=randint(1000, 5000), S=randint(1000, 5000), E=randint(1000, 5000), W=randint(1000, 5000)),
#          Fiona=dict(N=randint(1000, 5000), S=randint(1000, 5000), E=randint(1000, 5000), W=randint(1000, 5000)))
# for i in a:
#     print(i)
#     for y in a[i]:
#         print('\t', y, ':', a[i][y], sep='')
#
# l = input('Введите имя продавца: ')
# p = input('Введите регион: ')
# print(a[l][p])
# a[l][p] = input('Введите нужное значение: ')
# print(a[l])
# for i in a:
#     print(i)
#     for y in a[i]:
#         print('\t', y, ':', a[i][y], sep='')

# a = {"три": 3, "один": 1, "два": 2, "четыре": 4}
# b = {key: value for key, value in a.items() if value <= 2}
# print(b)
# for i in a.values():
#     print(i)
# s = [10, 20, 30, 40]
# s = "Hello"
# a = {i: i * 5 for i in s}
# print(a)
# v = int(input("-> "))
# s = [10, 20, 30, 40]
# a = {i: int(input("-> ")) for i in s}
# print(a)

# figure = {1: 'Rectangle', 2: 'Triangle', 3: "Circle"}
#
# print(list(figure))
# print(list(figure.values()))
# print(list(figure.items()))


# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = dict()
# s = None
#
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)

# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)

# a = ["Dec", "Jan", "Feb"]
# b = [12, 1, 2]
# c = [4.0, 5.0, 6.0]
# # f = {k: v for k, v in zip(b, a)}
# # print(f)
# z = zip(a, b, c)
# # print(z)
# # print(type(z))
# print(list(z))

# print(list(zip(range(2, 15), range(100))))
# a = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# b = {'a': 11, 'b': 22, 'c': 33, 'd': 44, 'e': 55}
# for (k1, v1), (k2, v2) in zip(a.items(), b.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)

# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs)
# print(a)
# print(b)

# a = ['b', 'c', 'a', 'd']
# b = [3, 2, 4, 1]
# data = list(zip(a, b))
# print(data)
# data.sort()
# print(data)
# data1 = list(zip(b, a))
# data1.sort()
# print(data1)
# data2 = sorted(zip(b, a))
# print(data2)

# month = ["January", "February", "March"]
# total_sales = [52000.00, 51000.00, 48000.00]
# production_cost = [46800.00, 45900.00, 43200.00]
# for sales, cost, m in zip(total_sales, production_cost, month):
#     res = sales - cost
#     print("Общая прибыль в", m, "=", res)

# one = {'apple': 0.04, 'orange': 0.35, 'pepper': 0.53}
# two = {'pepper': 0.20, 'onion': 0.55}
# print({**two, **one})  # {'apple': 0.04, 'orange': 0.35, 'pepper': 0.20, 'onion': 0.55}
# for k, v in {**two, **one}.items():
#     print(k, "->", v)

# colors = ["red", 'green', 'blue']
#
# ind = 1
# for color in colors:
#     print(str(ind) + ") " + color)
#     ind += 1
#
# print()
# for i, color in enumerate(colors, 1):
#     print(str(i) + ") " + color)


# d = {"a": 1, "b": 2, "c": 3, "d": 4}
#
# for i, (j, q) in enumerate(d.items(), 1):
#     print(i, ": ", j, "\t", q, sep="")

# d = {
#     1: {"a": 1, "b": 2, "c": 3, "d": 4},
#     2: {"a": 10, "b": 20, "c": 30, "d": 40}
# }
#
# for i, k in enumerate(d, 1):
#     print(i, ") key=", k, ", value=", d[k], sep="")

# num = [1, 2, 3, 4, 5]
# itr = iter(num)
# print(itr)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr, "STOP"))
# print(next(itr, "STOP"))

# a = [6, 7, 3, 4, 1, 5]
# b = enumerate(a)
# c = next(b)
# # c1 = next(b)
# print(c)
# # print(c1)
# print(type(c))
# print(next(b))
# print(next(b))

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# def func(*args):
#     return args
#
#
# print(func(1))
# print(func(1, 3, 5, 'abc'))
# print(func())

# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#     return res
#
#
# a = summa(1, 2, 3, 4, 5, 6, 7)
# b = summa(1, 2, 3)
# print(a)
# print(b)

# def func(*a):
#     return {i: i for i in a}
#
#
# print(func(1, 2, 3, 4))
# print(func("gray", (2, 17), 3.11, -4))


# def ch(*args):
#     pass
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))

# def funct(*a):
#     r = sum(a) / len(a)
#     d = []
#     for i in a:
#         if i < r:
#             d.append(i)
#     print(r)
#     return d
#
#
# print(funct(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(funct(3, 6, 1, 9, 5))

# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))


# def func(student, *s):
#     print("Student name: " + student, end=" ")
#     # s = []
#     # for score in scores:
#     #     s.append(score)
#     print(*s, sep=", ")
#
#
# func("Igor", 100, 95, 88, 92, 99)
# func("Rick", 69, 96, 20, 33)
# def reverse_num(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_odd=False):
#     res = []
#     for i in args:
#         if not only_odd or (only_odd and i % 2 != 0):
#             res.append(reverse_num(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True))

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a='python'))

# def info(**data):
#     for key, value in data.items():
#         print(key, "is", value)
#     print()
#
#
# info(firstname="Irina", lastname="Saunal", age=22, phone=1124564789)
# info(firstname="Igor", lastname="Wood", email="igor@mail.ru", age=22, phone=1124564789, country="Russia")

# def func(a, *args, b=False, **kwargs):
#     return a, args, kwargs, b
#
#
# print(func(1, 2, 3, 4, x=11, y=12, z=13, b=True))

# def db(**kwargs):
#     my_dict.update(**kwargs)
#
#
# my_dict = {"one": "first"}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyes_color="gray")
# print("my_dict =", my_dict)

# def func1(*args):
#     print(args[0])
#
#
# def func2(**kwargs):
#     print(kwargs['one'])
#
#
# func1(1, 2, 3, 4, 5, 6)
# func2(one=123, two=456)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = {**x, 'one': 1, 'two': 2, **y}
# print(z)

# scope - область видимости

# name = "Tom"  # глобальная переменная
#
#
# def hi():
#     global name
#     name = "Sam"  # локальная переменная
#     print("Hello", name)
#
#
# def bye():
#     print("Good bye", name)
#
#
# print(name)
# hi()
# bye()
#
# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()  # 6
# print(i)

# def add_two(a):
#     x = 2
#
#     def add_some():
#         print("x =", x)
#         return a + x
#
#     return add_some()
#
#
# print(add_two(3))

# x = 4
#
#
# def fun():
#     print(x + 3)
#
#
# fun()

# import builtins
#
# names = dir(builtins)
#
# for t in names:
#     print(t)


# def outer_func(who):
#     print(who)
#
#     def inner_func():
#         print("Hello,", who)
#
#     inner_func()
#
#
# outer_func("World!")


# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print("Сумма внутренней функции:", a + b)
#
#     print("Значение внешней переменной a:", a)
#
#     fun2(4)
#
#
# fun1()


# x = 25
#
#
# def fn():
#     global t
#     a = 30
#
#     print("global:", x)
#
#     def inner():
#         nonlocal a
#         a = 35
#
#     inner()
#     print(a)
#     t = a
#
#
# fn()
# z = x + t
# print(z)


# def fn1():
#     x1 = 25
#
#     def fn2():
#         x1 = 33
#
#         def fn3():
#             nonlocal x1
#             x1 = 55
#
#         fn3()
#         print("fn2.x1 =", x1)
#
#     fn2()
#     print("fn1.x1 =", x1)
#
#
# fn1()


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))


# локальная переменная
# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#
#     s = 2 * (rect_square(a, b) + (rect_square(a, c) + (rect_square(c, b))))
#     return s
#
#
# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(1, 6, 8))


# глобальная переменная
# s = 0
#
#
# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#
#     global s
#     s = 2 * (rect_square(a, b) + (rect_square(a, c) + (rect_square(c, b))))
#     return s
#
#
# b = rect_paral_square(2, 4, 6)
# print(b)
# print(s)
# print(rect_paral_square(5, 8, 2))
# print(s)
# print(rect_paral_square(1, 6, 8))
# print(s)

# нелокальная переменна
# def rect_paral_square(a, b, c):
#     s = 0
#
#     def rect_square(i, j):
#         nonlocal s
#         s += i * j
#
#     rect_square(a, b)
#     rect_square(a, c)
#     rect_square(c, b)
#     return 2 * s
#
#
# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(1, 6, 8))

# Замыкания
# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner


# print(outer(5)(10))
# add5 = outer(5)
# print(add5(10))
# print(add5(4))
# add6 = outer(6)
# print(add6(10))


# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         b = b + "2"
#         a = a + 1
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func(n):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(n, s)
#
#     return inner
#
#
# res = func('Москва')
# res()
# res()
#
# res2 = func('Сочи')
# res2()
# res2()
#
# res()

# students = {
#     "Alice": 98,
#     "Bob": 67,
#     "David": 85,
#     "Chris": 75,
#     "Ella": 54,
#     "Fiona": 35,
#     "Grace": 69
# }
#
#
# def outer(lower, upper):
#     def inner(exam):
#         return {k: v for (k, v) in exam.items() if lower <= v < upper}
#
#     return inner
#
#
# a = outer(80, 100)
# b = outer(70, 80)
# c = outer(50, 70)
# d = outer(0, 50)
# print(a(students))
# print(b(students))
# print(c(students))
# print(d(students))

# def func_object(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#
#     return replace
#
#
# obj1 = func_object(5, 2)
# print(obj1.add())
#
# obj2 = func_object(5, 2)
# print(obj2.sub())
#
# obj3 = func_object(5, 2)
# print(obj3.mul())
#
# print(type(func_object))


# def func(x1, y1):
#     return x1 + y1
#
#
# print(func(1, 2))
#
# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)('a', 'b'))
#
# func1 = lambda x, y: x + y
# print(func1(1, 2))
# print(func1('a', 'b'))

#
# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# summ = lambda a=1, b=2, c=3: a + b + c
#
#
# print(summ())
# print(summ(10, 20))
#
# func = lambda *args: print(args)
#
# func(1, 2, 3, 4)
# print(func('a', 'b', 'c'))

# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#     print(t('abc'))
# def inc1(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# def inc2(n):
#     return lambda x: x + n
#
#
# inc = (lambda n: (lambda x: x + n))
#
# f = inc(42)
# print(f(2))
#
# print((lambda n: (lambda x: x + n))(42)(2))

# def outer(x):
#     def inner(y):
#         def inner_inner(z):
#             return x + y + z
#
#         return inner_inner
#     return

# print((lambda x: (lambda y: (lambda z: x + y + z)))(4)(6)(10))

# d = {'r': 10, 'b': 15, 'c': 4}
# list_d = list(d.items())
# print(list_d)
# list_d.sort(key=lambda i: i[0])
# print(list_d)

# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[0](12, 6)
# print(b)
# print(type((lambda x, y: x + y)))

# players = [{'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#            {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#            {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#            {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6}]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
#
# res = sorted(players, key=lambda item: item['rating'])
# print(res)
#
# res = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res)

# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 1]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d = {
#     1: lambda: print('Monday'),
#     2: lambda: print('Tuesday'),
#     3: lambda: print('Wednesday'),
#     4: lambda: print('Thursday'),
#     5: lambda: print('Friday'),
#     6: lambda: print('Saturday'),
#     7: lambda: print('Sunday')
# }
#
# d[7]()

# area = {
#     'Circle': lambda r: pass,
#     'Rectangle': lambda ,
#     'Trapezoid': lambda
# }
# import math
#
# d = {
#     1: lambda x: print(math.pi * x ** 2),
#     2: lambda x, y: print(x * y),
#     3: lambda a, b, h: print((a + b) * h / 2)
# }
# d[1](12)
# d[2](2, 5)
# d[3](4, 7, 10)

# print((lambda a, b: a if a > b else b)(12, 13))
# print((lambda x, y, z: min(x, y, z))(6, 2, 18))
# print((lambda x, y, z: x if (x <= y) and (y <= z) else (y if (y <= x) and (y <= z) else z))(16, 12, 8))


# map(func, iterable)
#
# def mul(t):
#     return t * 2
#
#
# s = [2, 8, 12, -5, -8]
#
# ls = list(map(mul, s))
# print(ls)

# s = (2, 8, 12, -5, -8)
# print(tuple(map(lambda t: t * 2, (2, 8, 12, -5, -8))))

# s = ['1', '2', '3', '4', '5']
# print(type(s[0]))
# s1 = list(map(int, s))
# print(s1)
# print(type(s1[0]))

# areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.000135, 78.134165456465]
# res = list(map(round, areas, range(1, len(areas))))
# print(res)
#
# print(round(5.2345641, 3))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print(list(map(lambda x, y: x + y, l1, l2)))
#
# print(list(map(lambda x, y: x + y, [1, 5, 8], [2, 6, 1])))

#  filter(func, iterable)

# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
#
# print(tuple(filter(lambda s: len(s) == 3, t)))

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# # c = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)
# from random import randint
#
# # b = [randint(0, 40) for i in range(10)]
# # print(b)
# b = [45, 55, 60, 37, 100, 105, 220]
# # print(list(filter(lambda x: 20 >= x >= 10, b)))
# res = list(filter(lambda i: i % 15 == 0, b))
# print(res)
# res = list(filter(lambda i: not i % 15, b))
# print(res)

# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, range(10)))))
# print([x ** 2 for x in range(10) if x % 2 != 0])

# words = ('madam', 'fire', 'tomato', 'book', 'kiosk', 'mom')
# print(list(filter(lambda i: i == i[::-1], words)))

# Декораторы

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_hello'")
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# test = hello
# print(test)
# print(test())

# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return func_wrapper
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):  # декорирующая функция
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return func_wrapper
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# @my_decorator
# def hello():
#     print("Hello, I am func 'hello'")
#
#
# func_test()
# hello()
# test = my_decorator(func_test)
# test()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())
# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count = count + 1
#         fn()
#         print("Вызов функции: ", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()
# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Лаврова")
# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
#
# print_full_name("Борис", "Елизавета", "Светлана", study="JavaScript")
# print_full_name("Владимир", "Екатерина", "Виктор")

# def args_decorator(arg1, arg2):  # "Игорь", "Нефедов"
#     print("Аргументы:", arg1, arg2)
#
#     def wrapper(func1):  # функция
#
#         def wrap(func_arg1, func_arg_2):  # "Ирина", "Лаврова"
#             print("Аргументы функции", func_arg1, func_arg_2)
#             func1(func_arg1, func_arg_2)
#             func1(arg1, arg2)
#
#         return wrap
#
#     return wrapper
#
#
# @args_decorator("Игорь", "Нефедов")
# def func(first, last):
#     print("Меня зовут:", first, last)
#
#
# func("Ирина", "Лаврова")
# def args_decorator(decorator_text):
#     def wrapper(func):
#         def wrap(*args):
#             print(decorator_text, end="")
#             func(*args)
#             print()
#
#         return wrap
#     return wrapper
#
#
# @args_decorator(decorator_text="Hello, ")
# def hello_world(text):
#     print(text)
#
#
# @args_decorator(decorator_text="Hi, ")
# def hello(text, t2):
#     print(text, "and", t2)
#
#
# hello_world("world!")
# hello("Igor", "Irina")

# def multiply(a):
#     def wrapper(func):
#         def wrap(b):
#             return a * func(b)
#
#         return wrap
#
#     return wrapper
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))
# def typed(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Некорректный тип данных")
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Некорректный тип данных")
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# #
# # @typed(int, int, int)
# # def typed_fn(x, y, z):
# #     return x * y * z
# #
# #
# # @typed(str, str, str)
# # def typed_fn2(x, y, z):
# #     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello! "):
#     return (x + y) * z
#
#
# # print(typed_fn(3, 4, 5))
# # # print(typed_fn(3, 4, "Hello"))
# # print(typed_fn2("Hello, ", "world", "!"))
# # print(typed_fn2("Hello, ", "world", 2))
# print(typed_fn3("Hello, ", "world!  ", z=5))

# def decor(tx=None, dec_text=""):
#     def wrapper(func):
#         def wrap(*args):
#             print(dec_text, end="")
#             func(*args)
#
#         return wrap
#
#     if tx is None:
#         return wrapper
#     else:
#         return wrapper(tx)
#
#
# @decor
# def hello_world2(text):
#     print(text)
#
#
# hello_world2("Hi!")
#
#
# @decor(dec_text="Hello, ")
# def hello_world(text):
#     print(text)
#
#
# hello_world("world!")

# print(int('19'))
# print(int('19.5'))

# print(int("100", 2))
# print(int("100", 8))
# print(int("100", 10))
# print(int("100", 16))

# print(bin(18))  # 0b10010
# print(oct(18))  # 0o22
# print(hex(18))  # 0x12
#
# print(0b10010)
# print(0o22)
# print(0x12)

# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
# print(e * 3)
# print(e * -3)
# print(e in "I am learning Python")
# print(e in "I am learning Java")

# s = "Hello"
# print(s[::-1])
# print(s[1])
# print(s[-5])
# print(s[-6])

# s = 'abcdefgh'
#
# print(s[slice(2, 5)])
# print(s[slice(5, None, -1)])
# print(s[slice(None, None, 2)])
# print(s[slice(None, None, -1)])

# s = "python"
# print(id(s))
# s = s[:3] + 't' + s[4:]
# print(id(s))
# print(s)  # pytton

def change_char_to_str(s, old, new):
    s2 = ""
    i = 0

    while i < len(s):
        if s[i] == old:
            s2 = s2 + new
        else:
            s2 = s2 + s[i]
        i = i + 1

    return s2


str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
str2 = change_char_to_str(str1, "N", "P")
print("str1 =", str1)
print("str2 =", str2)
