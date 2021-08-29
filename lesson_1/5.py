"""
5. Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться
фиксированная ежемесячная сумма пополнения вклада. Необходимо в главной функции реализовать вложенную функцию
подсчета процентов для пополняемой суммы. Примем, что клиент вносит средства в последний день каждого месяца,
кроме первого и последнего. Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев.
Вложенная функция возвращает сумму дополнительно внесенных средств (с процентами), а главная функция — общую сумму по
вкладу на конец периода.
"""


def get_year_rate(amount, period):

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

    print('Сумма не подходит ни под один тариф')
    return None


def deposit(amount, period, charge=0):
    # Можно было бы просто добавить условие по месяцам и расчет внесенных средств в цикл расчета депозита
    # Но по заданию, необходимо реализовать вложенную функцию подсчета процентов для пополняемой суммы
    def sum_charge(charge_, period_, year_rate_):
        total_charge_ = charge_
        for _ in range(period_ - 2):  # Исключение первого и последнего месяца периода
            total_charge_ += total_charge_ * year_rate_ / 12
        return total_charge_

    year_rate = get_year_rate(amount, period)
    if not year_rate:
        print('Процентная ставка (тариф) не найдена')
        return None

    total, total_charge = amount, charge
    for month in range(period):
        total += total * year_rate / 12
    if charge:
        total_charge = sum_charge(charge, period, year_rate)
    total = total + total_charge

    return round(total, 2)


print(deposit(13400, 6, 2000))
