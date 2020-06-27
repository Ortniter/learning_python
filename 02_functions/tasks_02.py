def letters_check(password):
    if password.isalnum():
        if password.isascii():
            return 1
        return 'contains forbidden chars'
    return 'contains forbidden chars'


def even_letters(password):
    letters = ''
    for char in password:
        if char.isalpha():
            letters += char
    if len(letters) % 2:
        return 'quantity of letters is not even'
    else:
        return 1


def even_digits(password):
    digits = ''
    for digit in password:
        if digit.isdigit():
            digits += digit
    if len(digits) % 2:
        return 1
    else:
        return 'quantity of digits is even'


def validate_password(password):
    """
    Функция принимает пароль строкой и выполняет валидацию с помощью трёх
    вспомогательных функций:
    1. Содержит только a−z, A−Z, 0−9
    2. Содержит четное количество букв
    3. Содержит нечетное количество цифр
    Основная функция возвращает True, если пароль валидный.
    Если пароль не валидный, возвращает лист стрингов, в которых перечислены
    причины неуспешной проверки. Например: ["содержит запрещенные символы"]
    """
    list_of_checks = [letters_check(password), even_letters(
        password), even_digits(password)]
    list_of_errors = list()
    for elem in list_of_checks:
        if elem == 1:
            continue
        else:
            list_of_errors.append(elem)

    if len(list_of_errors) >= 1:
        return list_of_errors
    return True


def int_converter(input_int):
    """
    Функция принимает число и конвертирует его в 4 форматах:
    decimal, octal, binary, hexadecimal. Каст в форматы описан в документации.
    При касте нужно избавляться от первых символов (0o31 -> 31, 0xe6 -> e6).
    Возвращает строку, отформатированную с помощью функции print_table.
    """

    row1 = ["Decimal", "Octal", "Binary", "Hexadecimal"]
    row2 = [input_int, oct(input_int)[2:], bin(
        input_int)[2:12], hex(input_int)[2:12]]
    return print_table(4, 2, [row1, row2])


def print_table(cols=1, rows=1, *data):
    """
    Функция генерирует псевдотаблицу текстом.
    :cols: количество колонок в таблице
    :rows: количество строк в таблице
    :*data: лист листов, где каждый вложенный лист - строка данных.
    Пример: print_table(cols=4, rows=2, [["Decimal", "Octal", "Binary", "Hexadecimal"], [230, 346, 11100110, "e6"]])
    Вернет строку вида:
     -----------------------------------------------------------
    | Decimal      | Octal        | Binary       | Hexadecimal  |
    | 230          | 346          | 11100110     | e6           |
     -----------------------------------------------------------
    Форматирование должно полностью совпадать с примером.
    Обратить внимание на размеры ячеек - 12 символов на текст + по 1 вокруг
    слева и справа от разделителя |.
    """
    string = '---------------'
    data = data[0]
    line = ' ' + (string * cols)[:-1] + '\n'
    lst_rows = list()
    lst_rows.append(line)
    for row in data:
        new_row = list()
        for elem in row:
            new_row.append(str(elem)[:12].ljust(12) + ' | ')
        string = '| ' + ''.join(new_row) + '\n'
        lst_rows.append(string)
    lst_rows.append(line)
    new_str = ''.join(lst_rows)

    return new_str


print(int_converter(230))
