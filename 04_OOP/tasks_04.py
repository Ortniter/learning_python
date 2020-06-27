'''У вас есть список(list) IP адрессов. Вам необходимо создать
класс который сможет:
1) Получить и изменить список IP адресов
2) Получить список IP адресов в развернутом виде
(10.11.12.13 -> 13.12.11.10)
3) Получить список IP адресов без первых октетов
(10.11.12.13 -> 11.12.13)
4) Получить список последних октетов IP адресов
(10.11.12.13 -> 13)'''


class IpHandler:
    """Handles a list of IPs, each IP must be a string"""

    def __init__(self, ipList):
        self._ipList = ipList

    @property
    def ipList(self):
        return self._ipList

    @ipList.setter
    def ipList(self, newList):
        self._ipList = newList

    def reverse_IP(self):
        """Return it's IPs reversed"""
        reversed_ips = list()
        for ip in self.ipList:
            new_ip = '.'.join(reversed(ip.split('.')))
            reversed_ips.append(new_ip)
        return reversed_ips

    def get_oct_1_3(self):
        """Returns a list of IPs without first octets (127.0.0.1 -> .0.0.1)"""
        oct_1_3 = list()
        for ip in self.ipList:
            new_ip = '.'.join(ip.split('.')[1:4])
            oct_1_3.append(new_ip)
        return oct_1_3

    def get_oct_3(self):
        """Returns a list of last octets of each IP (127.0.0.1 -> .1)"""
        oct_3 = list()
        for ip in self.ipList:
            new_ip = '.'.join(ip.split('.')[3:])
            oct_3.append(new_ip)
        return oct_3


'''У вас несколько JSON файлов. В каждом из этих файлов есть
произвольная структура данных. Вам необходимо написать
класс (без реализации конструктора) который будет описывать работу с
этими файлами, а именно:
1) Запись в файл
2) Чтение из файла
3) Получить путь относительный путь к файлу
4) Получить абсолютный путь к файлу'''

import os


class JSONhandler:
    """Handles .json files: read, write, get abs/rel path"""

    def read(self, file):
        """Reads json file"""
        with open(file, 'r') as json:
            return json.read()
            # or
            # print(json.read())

    def write(self, input_data, file):
        """Writes json-formatted data to provided file"""
        with open(file, 'w') as json:
            json.write(input_data)
            print('Data has been written')

    def get_absolute_path(self, file):
        """Returns absolute path to provided file"""
        abspath = os.path.abspath(file)
        return abspath

    def get_relative_path(self, file):
        """Returns relative path to provided file"""
        relpath = os.path.relpath(file)
        return relpath


'''Создайте класс который будет хранить параметры для
подключения к физическому юниту (например сервер). В своем
списке атрибутов он должен иметь минимальный набор
(unit_name, mac_address, ip_address, login, password).
Вы должны описать каждый из этих атрибутов в виде гетеров и
сеттеров (@property). У вас должна быть возможность
получения и назначения этих атрибутов в классе.'''


class ConnHandler:
    __slots__ = ['_unit_name', '_mac_address',
                 '_ip_address', '_login', '_password']

    def __init__(self, unit_name='', mac_address='', ip_address='', login='', password=''):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password

    @property
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, new_unit):
        self._unit_name = new_unit

    @property
    def mac_address(self):
        return self._mac_address

    @mac_address.setter
    def mac_address(self, new_mac):
        self._mac_address = new_mac

    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, new_ip):
        self._ip_address = new_ip

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, new_login):
        self._login = new_login

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = new_password


'''Создать класс для представления информации о времени. Ваш класс должен иметь
возможности установки времени и изменения его отдельных полей (час, минута,
секунда) с проверкой допустимости вводимых значений. В случае недопустимых
значений полей нужно установить максимально допустимое значение.
Создать методы изменения времени на заданное количество часов, минут и секунд.'''


class Time:
    def __init__(self, h=0, m=0, s=0):
        self._hours = h if h in range(0, 23) else 23
        self._minutes = m if m in range(0, 59) else 59
        self._seconds = s if s in range(0, 59) else 59

    def __repr__(self):
        return f'{self.hours}.{self.minutes}.{self.seconds}'

    def __str__(self):
        return f'{self.hours}.{self.minutes}.{self.seconds}'

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, new_h):
        new_h = 23 if new_h not in range(0, 23) else new_h
        self._hours = new_h

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, new_m):
        new_m = 59 if new_m not in range(0, 59) else new_m
        self._minutes = new_m

    @property
    def seconds(self):
        return self._seconds

    @seconds.setter
    def seconds(self, new_s):
        new_s = 59 if new_s not in range(0, 59) else new_s
        self._seconds = new_s


'''Создайте класс Student, который содержит атрибуты: фамилия и инициалы, номер
группы, успеваемость (массив из пяти элементов).
Создайте список студентов из десяти элементов (10 экземпляров вашего класса).
Напиши функции:
1. Упорядочить массив по возрастанию среднего балла.
2. Вывести фамилии и номера групп студентов, имеющих оценки, равные
только 4 или 5.'''


class Student(object):
    def __init__(self, name, group_number, marks):
        self.name = name
        self.group_number = group_number
        self.marks = marks

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


from random import choice


def random_marks():
    marks = [1, 2, 3, 4, 5]
    random_lst = []
    while len(random_lst) != 5:
        random_lst.append(choice(marks))
    return random_lst


students_lst = [
    Student('Webb M.J.', 1, [5, 5, 5, 5, 5]),
    Student('Williamson K.J.', 3, random_marks()),
    Student('Cooper N.L.', 1, random_marks()),
    Student('Guido I.J.', 2, random_marks()),
    Student('Adams J.F.', 2, random_marks()),
    Student('Watson Y.W.', 3, random_marks()),
    Student('Fisher F.O.', 1, random_marks()),
    Student('Carter M.D.', 2, random_marks()),
    Student('Anderson A.E.', 3, random_marks()),
    Student('Edwards H.H.', 3, random_marks())
]


def get_best_by_mark(s_list):
    string = 'Best students:\n'
    for obj in s_list:
        if set(obj.marks) == {4, 5}:
            string += f'Student - "{obj.name}" Group - {obj.group_number}\n'
        elif set(obj.marks) == {4}:
            string += f'Student - "{obj.name}" Group - {obj.group_number}\n'
        elif set(obj.marks) == {5}:
            string += f'Student - "{obj.name}" Group - {obj.group_number}\n'
        else:
            continue
    print(string)


def sort_by_avg_mark(s_list):
    marks_dict = dict()
    for obj in s_list:
        avg = sum(obj.marks) // len(obj.marks)
        marks_dict[obj] = avg
    sort = sorted(marks_dict.items(), key=lambda item: item[1])
    avg_lst = [i[0] for i in sort]
    return avg_lst