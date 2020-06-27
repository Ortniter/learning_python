def catalog_finder(url_list):
  """
  Дописать функцию, которая принимает список URL, а возвращает
  список только тех URL, в которых есть /catalog/
  """

  result_list = [i for i in url_list if '/catalog/' in i]

  return result_list


# catalog_urls = ['https://www.grammarly.com/blog/catalog/', 'https://www.merriam-webster.com/dictionary/catalog/',
#                 'https://docs.python.org/3/', 'https://www.worldcat.org/catalog/', 'https://github.com']
# print(catalog_finder(catalog_urls))


#####################################################


def idiotic_str(input_str):
  """
  Вернуть полученную строку, сделав каждую вторую букву заглавной:
  Пример: тестовая строка -> тЕсТоВаЯ СтРоКа
  """
  idiotic_str = ''
  count = 0
  for i in input_str:
    count += 1
    if count % 2 == 0:
      idiotic_str += i.upper()
    else:
      idiotic_str += i.lower()
  return idiotic_str


# string = 'pineapple'
# print(idiotic_str(string))


#####################################################


def get_str_center(input_str):
  """
  Дописать функцию, которая вернет Х символов из середины строки
  (2 для четного кол-ва символов, 3 - для нечетного).
  """
  if len(input_str) < 2:
    return 'give me a longer string'
  else:
    if len(input_str) % 2 != 0:
      n = len(input_str) // 2
      output_str = input_str[n - 1:n + 2]
    else:
      n = len(input_str) // 2
      output_str = input_str[n - 1:n + 1]

    return output_str


string = 'UKRAINE'
print(get_str_center(string))


#####################################################


def count_symbols(input_str):
  """
  Дописать функцию, которая считает сколько раз каждая из букв
  встречается в строке, разложить буквы в словарь парами
  {буква:количество упоминаний в строке}
  """
  output_dict = dict()
  for i in input_str:
    if i not in output_dict.keys():
      output_dict[i] = 1
    else:
      output_dict[i] += 1
  return output_dict


# string = 'hello, python'
# print(count_symbols(string))


#####################################################


def mix_strings(str1, str2):
  """
  Дописать функцию, которая будет принимать 2 строки и вставлять вторую
  в середину первой
  """
  middle = len(str1) // 2
  result_str = str1[:middle] + str2 + str1[middle:]
  return result_str


# string1 = 'USSR'
# string2 = 'USA'
# print(mix_strings(string1, string2))


#####################################################


def avg_score(score_list):
  """
  Дописать функцию, которая принимает список строк с оценками, а возвращает
  список строк со средним баллом
  Пример: ["Mike|83, 90, 34, 54", "Jane|45, 46, 53, 23"] ->
  ["Mike|65", "Jane|42"]
  """
  # your code here
  avg_scores = list()
  for student in score_list:
    ints_lst = list()
    splited_scores = student.split(', ')
    for elem in splited_scores:
      if '|' in elem:
        name = elem.split('|')[0]
        ints_lst.append(int(elem.split('|')[1]))
      else:
        ints_lst.append(int(elem))

    mark = f'{name}|{sum(ints_lst) // len(ints_lst)}'

    avg_scores.append(mark)

  return avg_scores


# scores = ["Mike|83, 90, 34, 54", "Jane|45, 46, 53, 23"]
# print(avg_score(scores))


#####################################################


# Мой первый убогий вариант этой функции:


def encrypt_str(input_str):
  """
  Дописать функцию, которая будет шифровать полученную строку следующим
  образом:
  Пример 1: "www" -> "w3"
  Пример 2: "abbbccdeffgggg" -> "ab3c2def2g4"
  """
  example = input_str[0]
  lst = []
  new_str = ''
  for i in input_str + '?':
    if i == example:
      lst.append(i)
    elif i != example:
      if len(lst) == 1:
        example = i
        new_str += str(lst[0])
        lst.clear()
        lst.append(i)
      else:
        example = i
        new_str += str(lst[0]) + str(len(lst))
        lst.clear()
        lst.append(i)
    elif i == '?':
      if len(lst) == 1:
        new_str += str(lst[0])
        lst.clear()
      else:
        new_str += str(lst[0]) + str(len(lst))
        lst.clear()
  return new_str


# string = "abbbccdeffgggg"
#
# print(encrypt_str(string))


# Мой второй убогий вариант этой функции:


def encrypt_str(input_str):
  """
  Дописать функцию, которая будет шифровать полученную строку следующим
  образом:
  Пример 1: "www" -> "w3"
  Пример 2: "abbbccdeffgggg" -> "ab3c2def2g4"
  """
  encrypted_str = ''
  output_dict = dict()
  for i in input_str:
    if i not in output_dict.keys():
      output_dict[i] = 1
    else:
      output_dict[i] += 1

  for key, value in output_dict.items():
    if value == 1:
      encrypted_str += f'{key}'
    else:
      encrypted_str += f'{key}{value}'

  return encrypted_str

# string = "abbbccdeffgggg"
#
# print(encrypt_str(string))

#####################################################


def square_dict(input_dict):
  """
  Сгенерировать dict() из списка ключей ниже по формуле (key : key*key).
  keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  ожидаемый результат: {1: 1, 2: 4, 3: 9 …}
  """
  squared_dict = dict()
  for number in input_dict:
    squared_dict[number] = number * number
  return squared_dict


# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(square_dict(lst))


#####################################################


import random


def even_int_generator():
  """
  Сгенерировать список из диапазона чисел от 0 до 100 и записать
  в результирующий список только четные числа.
  """
  # your code here
  even_int_list = [i for i in range(random.randint(0, 100)) if i % 2 == 0]
  return even_int_list


# print(even_int_generator())


#####################################################

from random import choice


def replace_vowels(input_str):
  """
  Заменить в произвольной строке согласные буквы на гласные.
  """
  letters = []
  for char in input_str:
    if char.lower() not in 'qwrtpsdfghjkzxcvbnml':
      letters.append(char)
    else:
      letters.append(random.choice(['E', 'Y', 'U', 'I', 'O', 'A']))
  result_str = ''.join(letters)
  return result_str


# string = 'Hello, Python'
# print(replace_vowels(string))


#####################################################


def filter_unique_int(input_list):
  """
  Дан массив чисел.
  [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
  убрать из него повторяющиеся элементы
  """
  # your code here
  unique_int_list = list(set(input_list))
  return unique_int_list


# lst = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
# print(filter_unique_int(lst))


#####################################################


def three_biggest_int(input_list):
  """
  Дан массив чисел.
  [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
  вывести 3 наибольших числа из исходного массива
  """
  biggest_ints = list()
  for i in range(3):
    index = input_list.index(max(input_list))
    biggest_ints.append(str(input_list.pop(index)))

  return ', '.join(biggest_ints)


# lst = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
# print(three_biggest_int(lst))


#####################################################


def lowest_int_index(input_list):
  """
  Дан массив чисел.
  [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
  вывести индекс минимального элемента массива
  """
  # your code here
  lowest_index = input_list.index(min(input_list))
  return lowest_index


# lst = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
# print(lowest_int_index(lst))


#####################################################


def reversed_list(input_list):
  """
  Дан массив чисел.
  [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
  вывести исходный массив в обратном порядке
  """
  # your code here
  reversed_lst = list(reversed(input_list))
  return reversed_lst


# lst = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
# print(reversed_list(lst))


#####################################################


def find_common_keys(dict1, dict2):
  """
  Найти общие ключи в двух словарях, вернуть список их названий
  """
  common_keys = list()
  for key in dict1.keys():
    if key in dict2:
      common_keys.append(key)
  return common_keys


# d1 = {'name': 'Carl', 'number': '23', 'part': 1, 'mode': 'on'}
# d2 = {'mode': 'off', 'part': 23, 'surname': 'Clinton'}
#
# print(find_common_keys(d1, d2))


#####################################################


def removekey(d, key):
  r = dict(d)
  del r[key]
  return r


def sort_by_age(student_list):
  """
  Дан массив из словарей. C помощью sort() отсортировать массив из словарей
  по значению ключа 'age', сгруппировать данные по значению ключа 'city'
  вывод должен быть такого вида :
      {
         'Kiev': [ {'name': 'Viktor', 'age': 30 },
                      {'name': 'Andrey', 'age': 34}],
         'Dnepr': [ {'name': 'Maksim', 'age': 20 },
                         {'name': 'Artem', 'age': 50}],
         'Lviv': [ {'name': 'Vladimir', 'age': 32 },
                      {'name': 'Dmitriy', 'age': 21}]
      }
  """
  sorted_lst = sorted(student_list, key=lambda person: person['age'])

  sorted_dict = dict()

  for element in sorted_lst:
    sorted_dict[element['city']] = sorted_dict.get(element['city'], [])
    sorted_dict[element['city']].append(removekey(element, 'city'))

  return sorted_dict


# lst = [{'name': 'Viktor', 'age': 30, 'city': 'Kiev'}, {'name': 'Andrey', 'age': 34, 'city': 'Kiev'},
#        {'name': 'Maksim', 'age': 20, 'city': 'Dnepr'}, {'name': 'Artem', 'age': 50, 'city': 'Dnepr'},
#        {'name': 'Vladimir', 'age': 32, 'city': 'Lviv'}, {'name': 'Dmitriy', 'age': 21, 'city': 'Lviv'}
#        ]
#
# print(sort_by_age(lst))
