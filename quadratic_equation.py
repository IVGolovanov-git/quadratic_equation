# Решение квадратного уравнения ax**2 + bx + c

# Ввод переменных в режиме теста
# var_a = 1
# var_b = 6
# var_c = 5

# Ввод переменных с консоли
var_a = int(input('Веедите переменную а = ',))
var_b = int(input('Веедите переменную b = ',))
var_c = int(input('Веедите переменную c = ',))

# Решение при a = 0
if var_a == 0:
    print('\033[1m \nРешение при а=0:\033[0m') # \n\033[1m - выдел стр жирным
    if var_b == 0:
        print(f'Корней в уравнении нет')
    else:
        root = - var_c / var_b
        print(f'Единственный корень уравнения: {round(root, 2)}')

# Решение при с=0
if var_c == 0 and var_a != 0:
    print('\033[1m \nРешение при c=0:\033[0m')
    root_one = 0
    root_two = -var_b / var_a
    print(f'Первый корень = {root_one} \nВторой корень = {round(root_two, 2)}')

# Решение при b=0
if var_b==0 and var_a != 0:
    print('\033[1m \nРешение при b=0:\033[0m')
    var_under_square = -var_c / (var_a)
    print(f' VAS = { round(var_under_square,2) }')
    if var_under_square >= 0:
        root_one = var_under_square**0.5
        root_two = - (var_under_square**0.5)
        print(f'Первый корень = {root_one} \nВторой корень = {round(root_two, 2)}')
    if var_under_square < 0:
        print(f'Уравнение не имеет корней')

# Решение по полной формуле
if var_a != 0 and var_b !=0 and var_c !=0:
    print('\033[1m \nРешаем по полной формуле:\033[0m')
    discriminant = var_b**2 - 4*var_a*var_c

    if discriminant >= 0:
        root_one = (-var_b + discriminant ** 0.5) / (2 * var_a)
        root_two = (-var_b - discriminant ** 0.5) / (2 * var_a)
        print(f'Первый корень = {round(root_one, 2)}')
        print(f'Второй корень = {round(root_two, 2)}')
