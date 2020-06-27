# 0. arabic to rome


# def correct_input(func):
#     def wrapper(*args):
#         if args[0] > 2020:
#             print('Function accepts only ints that less than or equal to 2020')
#         elif args[0] < 1:
#             print('Please input smth greater than 0')
#         else:
#             return func(*args)

#     return wrapper


# @correct_input
# def arabic_to_roman(number):
#     num_dict = {'units': {1: 'I', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'},
#                 'dozens': {1: 'X', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'},
#                 'hundreds': {1: 'C', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'},
#                 'thousands': {1: 'M'}}
#     values_lst = [(num_dict['thousands'], 1000, 'M'), (num_dict['hundreds'], 100, 'C'),
#                   (num_dict['dozens'], 10, 'X'), (num_dict['units'], 1, 'I')]
#     answer = ''
#     for n_dict, value, roman in values_lst:
#         amount = number // value
#         numbers = ''.join(
#             [n_dict[amount] if amount in n_dict else amount * roman])
#         answer += numbers
#         number = number % value
#     return answer


# result = arabic_to_roman(1622)
# print(result)


# 1. Написать свой cache декоратор c максимальным размером кеша и его очисткой
# при необходимости.


# def do_cache(maxsize):
#     def decorator(func):
#         cache = dict()  # этот дикт будет доступен при следующих вызовах

#         def wrapper(*args):
#             if len(cache) >= maxsize:
#                 # Если количество закешированных элементов превышает maxsize,
#                 # нужно удалить самый первый закешированный элемент.
#                 from random import choice
#                 random_key = choice(list(cache.keys()))
#                 del cache[random_key]
#             if args in cache:
#                 # Если элемент уже есть в кеше, нужно вернуть его, не вызывая
#                 # декорируемой функции
#                 return cache[args]
#             else:
#                 # Если элемента нет в кеше, нужно вызвать декорируемую функцию,
#                 # сохранить ее результат в кеш и вернуть ее результат
#                 answer = func(*args)
#                 cache[args] = answer
#                 print(cache)
#                 return answer

#         return wrapper

#     return decorator


# @do_cache(maxsize=3)
# def test(v, i):
#     return v + i


# 2. Написать свой декоратор который будет проверять остаток от деления числа 100
# на результат работы функции ниже. Если остаток от деления = 0, вывести
# сообщение "We are OK!», иначе «Bad news guys, we got {остаток от деления}».
# Этот декоратор не должен возвращать результат работы функции. Только один из
# указанных принтов.

# def div100(func):
#     def wrapper(*args):
#         answer = 100 % func(*args)
#         if answer:
#             print(f'Bad news guys, we got {answer}')
#         else:
#             print('We are OK!')
#         # your code here

#     return wrapper


# @div100
# def test2(v):
#     return v


# 3. Декоратор должен кэшировать значения аргументов, считать количество
# использований одних и тех же аргументов и печатать их перед исполнением
# декорируемой функции.

# def count_args(func):
#     cache_count = dict()  # этот дикт будет доступен при следующих вызовах

#     def wrapper(*args):
#         if args not in cache_count:
#             cache_count[args] = 1
#         else:
#             cache_count[args] += 1
#         if cache_count[args] > 1:
#             print(f'"{args[0]}" was used  {cache_count[args]} times')
#         else:
#             print(f'"{args[0]}" was used {cache_count[args]} time')
#         return func(*args)

#     return wrapper


# @count_args
# def my_func(string):
#     return string
