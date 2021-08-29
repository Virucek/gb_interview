"""
4. Написать программу «Банковский депозит». Она должна состоять из функции и ее вызова с аргументами. Клиент банка
делает депозит на определенный срок. В зависимости от суммы и срока вклада определяется процентная ставка:
1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых).
10000–100000 руб (6 месяцев — 6 % годовых,год — 7 % годовых, 2 года – 6.5 % годовых).
100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых,2 года — 7.5 % годовых).
Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада. Каждый из трех
банковских продуктов должен быть представлен в виде словаря с ключами (begin_sum, end_sum, 6, 12, 24).
Ключам соответствуют значения начала и конца диапазона суммы вклада и значения процентной ставки для каждого
срока. В функции необходимо проверять принадлежность суммы вклада к одному из диапазонов и выполнять расчет по нужной
процентной ставке. Функция возвращает сумму вклада на конец срока.
"""


def get_rate(amount, period):

    months = [6, 12, 24]
    rates = [
        {'begin_sum': 1000, 'end_sum': 10000, months[0]: 5, months[1]: 6, months[2]: 5},
        {'begin_sum': 10000, 'end_sum': 100000, months[0]: 6, months[1]: 7, months[2]: 6.5},
        {'begin_sum': 100000, 'end_sum': 1000000, months[0]: 7, months[1]: 8, months[2]: 7.5},
    ]
    if period not in months:
        print('Неверный период')
        return None

    for rate in rates:
        if rate['begin_sum'] <= amount < rate['end_sum']:
            return rate[period] / 100
    print('Сумма не подходит ни под один период')
    return None


def deposit(amount, period):

    rate = get_rate(amount, period)
    if not rate:
        print('Процентная ставка не найдена')
        return None

    total = amount
    for _ in range(period):
        total += total * rate / 12

    return round(total, 2)


print(deposit(13400, 6))