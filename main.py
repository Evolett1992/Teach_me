import os
from dotenv import load_dotenv

load_dotenv()

items = int(os.getenv('ITEMS'))
sum = float(os.getenv('SUM'))
order_num = int(os.getenv('ORDER_NUM'))

# ITEMS = 1
# SUM = 2.2
# ORDER_NUM = 333


# 1. Касса перепутала номер в очереди с суммой. Надо поменять эти переменные местами
sum, order_num = order_num, sum
print("sum = " + str(sum) + ";" "\n" + "order_num = " + str(order_num))

# Сначала поменяли значения местами, и отобразили принтом.
# ("text" + str()) используются чтобы добавить текст и после значение, str() в данном случае для приведения
# команды в одном формате (строка).
# "\n" - используется для перехода на следущюю строку.

print("_____________________")

# 2. Для отчёта боссу, нужно посчитать среднюю стоимость каждой пиццы в заказе
print("В среднем наша пица стоит: " + str(sum / order_num))

# для среднего значения колличество делится на цену

print("_____________________")

# 3. Если в сумме заказа нету дробей (.00), нужно, чтобы нули не отрисовывались
if sum != float(1):
    print("Пицца пепперони. Цена: " + str(int(sum // 1)))
    print("Спасибо за покупку!")

# Если (if) sum (переменная) !=(не равна) дробной от 1, то используем // для деления без остатка
# при этом используем int чтобы отобразить только целое число.

print("_____________________")

# 4. Если у клиента в номере заказа есть цифра 2, ему положена скидка в 50%
if order_num % 1 == int(2) or float(2):
    print(sum / 2)
    print("Подзравляем!Для вас скидка 50%")
else:
    print("Спасибо за покупку!")

# if(Если) order_num(переменная) делим на себя и проверяем есть ли целая цмфра 2(int) и дробная(float)
# Else(Иначе) -  пишем условия

print("_____________________")

# 5. Если кол-во пицц в заказе меньше 2, от номер в очереди нужно сократить на 5
if items < int(2):
    print(order_num - 5)
    print("Подзравляем!Подвинте тех петярых!Можно!")
else:
    print("Спасибо за покупку!")

# if(Если) items(переменная) меньше 2, int - для целого числа, отнимаем 5
# Else(Иначе) - пишем условия