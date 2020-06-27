def count_work_hours(in_time, out_time, rate):
    """
    Функция считает оплату за отработанные часы.
    :in_time int: время начала, в целых часах, например, 8
    :out_time int: время окончания, в целых часах, например, 19
    :rate float: стоимость полного часа
    Возвращает строку вида "57.63 for 9 hours"
    Если количество часов < 8, оплата не считается и равна 0.
    Если количество часов > 8, оплата за каждый сверхурочный час считается по
    полуторному рейту.
    """
    work_hours = out_time - in_time
    payment = 0.0
    if work_hours == 8:
        payment = rate * 8
    elif work_hours > 8:
        payment = 8 * rate + (work_hours - 8) * (rate * 1.5)
    return f'{payment} for {work_hours} hours'


def plan_trip(destination_list):
    """
    Функция считает стоимость путешествия.
    :destination_list list: список кортежей вида (длительность поездки, город),
    то есть, можно за один вызов посчитать несколько поездок.
    Возвращает цену для каждой поездки (float) списком.
    Стоимость путешествия = прямой перелет + обратный перелет + длительность *
    стоимость отеля.
    Цены:
    1. Получение стоимости отеля в заданном городе (за 1 ночь: Odesa - 33,
    Kyiv - 42, Larnaka - 49, Istanbul - 38);
    2. Получение стоимости перелета в заданный город или обратно (в 1 сторону:
    Odesa - 80, Kyiv - 97, Larnaka - 134, Istanbul - 149).
    """
    hotels_prices = {'Odesa': 33, 'Kyiv': 42, 'Larnaka': 49, 'Istanbul': 38}
    flights_prices = {'Odesa': 80, 'Kyiv': 97, 'Larnaka': 134, 'Istanbul': 149}
    costs = list()

    for place in destination_list:
        cost = place[0] * hotels_prices[place[1]] + flights_prices[place[1]] * 2
        costs.append(cost)

    # last_city = destination_list[-1][1]
    # new_cost = costs.pop(-1) + flights_prices[last_city]
    # costs.append(new_cost)

    return costs


# check = [(8, 'Odesa'), (4, 'Istanbul')]
#
# result = plan_trip(check)
# print(result)


from datetime import date

# database - список словарей, эмулирующий базу данных со строками и полями
database = list()


def check_chars(string):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    digits = '1234567890'
    allowed = set(alpha + digits + '-_.@')
    for i in set(string):
        if i not in allowed:
            return False
    return True


def check_email(email):
    if len(str(email)) == 0:
        return False
    elif '@' not in str(email):
        return False
    elif '.' not in str(email):
        return False
    else:
        at_index = email.index('@')
        dot_index = email[at_index + 2:].rfind('.')
        check_lst = [isinstance(email, str), len([i for i in email if i == '@']) == 1, check_chars(email),
                     '@' not in email[:1], '.' not in email[at_index + 1:at_index + 2],
                     len(email[at_index + 2:][dot_index + 1:]) <= 3]
    if False in check_lst:
        return False
    return True


def check_age(birth):
    if not isinstance(birth, date):
        return False
    elif len(str(birth)) == 0:
        return False
    else:
        today = date.today()
        age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
        check_lst = [birth <= date.today(), age <= 100]
    if False in check_lst:
        return False
    return True


def check_names(name, count):
    if count == 'first':
        check_lst = [isinstance(name, str), len(str(name)) != 0, len(str(name)) < 48]
    else:
        check_lst = [isinstance(name, str), len(str(name)) != 0, len(str(name)) < 64]
    if False in check_lst:
        return False
    return True


def validate_input(data: tuple) -> bool:
    """
    Функция принимает список словарей, валидирует каждый из словарей на наличие
    всех необходимых полей и тип их данных. Возвращает:
    1. bool в зависимости от результатов проверки;
    2. None или словарь, где ключ - тип ошибки (ValueError, KeyError),
    а значение - список кортежей вида (ключ с ошибкой, словарь полностью).
    Правила валидации:
    first_name - string, не пустой, короче 48 символов
    last_name - string, не пустой, короче 64 символов
    birth - date, не пустой, не в будущем, не старше 100 лет
    email - string, формат строка, затем @, затем опять строка, точка,
    строка от 2 до 3 символов
    Допустимые символы в email: буквы, цифры, символы (-_.)
    """
    reference = ['first_name', 'last_name', 'birth', 'email']
    key_errors = {'KeyError': list()}
    for row in data:
        if list(row.keys()) != reference:
            key_errors['KeyError'].append(row)
    if len(key_errors['KeyError']) != 0:
        handle_error(key_errors)
        return False

    value_errors = {'ValueError': []}
    for person in data:
        first_name = check_names(person['first_name'], 'first')
        if first_name == 0:
            value_errors['ValueError'].append({'first_name': person})

        last_name = check_names(person['last_name'], 'last')
        if last_name == 0:
            value_errors['ValueError'].append({'last_name': person})

        birth = check_age(person['birth'])
        if birth == 0:
            value_errors['ValueError'].append({'birth': person})

        email = check_email(person['email'])
        if email == 0:
            value_errors['ValueError'].append({'email': person})

    if len(value_errors['ValueError']) != 0:
        handle_error(value_errors)
        return False
    return True


def handle_error(error_dict) -> None:
    """
    Функция принимает словарь ошибок и проблемных словарей и принтит их.
    Пример:
    ValueError found in:
    {"first_name": {"first_name": 42, "second_name": "Van Rossum"}}
    {"second_name": {"first_name": "Guido", "second_name": 42}}
    """
    if 'KeyError' in error_dict.keys():
        errors = [str(i) for i in error_dict['KeyError']]
        errors_str = '\n'.join(errors)
        print(f'KeyError found in:\n{errors_str}')
    else:
        errors = [str(i) for i in error_dict['ValueError']]
        errors_str = '\n'.join(errors)
        print(f'ValueError found in:\n{errors_str}')


def save_to_db(data: tuple) -> bool:
    """
    Функция принимает кортеж словарей с данными, валидирует каждую запись с
    помощью вспомогательной функции validate_input, и если данные валидны,
    добавляет их в database.
    Возвращает bool по результатам успешного/неуспешного выполнения.
    """
    if validate_input(data):
        for row in data:
            database.append(row)
        return True
    return False


def select_from_db(field, value):
    """
    Функция возвращает кортеж словарей, где переданное значение встречается в
    переданном ключе.
    """
    needed_rows = list()
    for row in database:
        if field in list(row.keys()):
            if value == row[field]:
                needed_rows.append(row)
    return tuple(needed_rows)


test = ({"first_name": 'Guido', "last_name": "Van Rossum", "birth": date(1956, 1, 31), "email": "guido@python.com"},
        {"first_name": 'Stan', "last_name": "Lee", "birth": date(1922, 12, 28), "email": "stan_lee@gmail.com"})

result = save_to_db(test)
print(result)
print('______________')
print(database)
print('______________')
result_select = select_from_db('last_name', 'Lee')
print(result_select)
