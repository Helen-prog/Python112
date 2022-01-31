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
from random import choices
import random as r

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

import time

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

import locale

locale.setlocale(locale.LC_ALL, "ru")

print(time.strftime("Сегодня: %B %d, %Y", time.localtime()))

