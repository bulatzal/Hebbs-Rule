# Выполнение алгоритма Хебба
def hebbs_rule(neuron):
    neuron_type = neuron['Тип нейрона']  # Значение типа нейрона
    neuron_value1 = neuron['Изображение 1']['Значение']  # Значение изображения 1
    neuron_output1 = neuron['Изображение 1']['Выходной сигнал']  # Выходной сигнал изображения 1
    neuron_value2 = neuron['Изображение 2']['Значение']  # Значение изображения 2
    neuron_output2 = neuron['Изображение 2']['Выходной сигнал']  # Выходной сигнал изображения 2

    # Проверка на совпадение длины значений
    if len(neuron_value1) != len(neuron_value2):
        print('Длина букв не совпадает!')
        exit()  # Если длина не совпадает, то программа закрывается

    weight = (len(neuron_value1) + 1) * [0]  # Инициализация весовых коэффициентов

    if neuron_type == 'Биполярный':
        quality = 0  # Проверка качества (0 - если не прошла, 1 - если прошла)
        k = 1  # Количество итераций
        while quality == 0:
            print('Прогон первой буквы: ')
            weight = weight_calculation_bipolar(weight, neuron_value1, neuron_output1)
            print('w =', weight)
            print('Прогон второй буквы: ')
            weight = weight_calculation_bipolar(weight, neuron_value2, neuron_output2)
            print('w =', weight)
            print('Проверка качества обучения: ')
            quality = quality_checking(weight, neuron_value1, neuron_value2)
            k += 1
            print('Цель достигнута за', k - 1, 'итераций! \nКонечный w =', weight) if quality == 1 else print(
                'Цель не достигнута. Начинается повтор', k)
    elif neuron_type == 'Бинарный':
        quality = 0  # Проверка качества (0 - если не прошла, 1 - если прошла)
        k = 1  # Количество итераций
        while quality == 0:
            print('Прогон первой буквы: ')
            weight = weight_calculation_binary(weight, neuron_value1, neuron_output1)
            print('w =', weight)
            print('Прогон второй буквы: ')
            weight = weight_calculation_binary(weight, neuron_value2, neuron_output2)
            print('w =', weight)
            print('Проверка качества обучения: ')
            quality = quality_checking(weight, neuron_value1, neuron_value2)
            k += 1
            print('Цель достигнута за', k - 1, 'итераций! \nКонечный w =', weight) if quality == 1 else print(
                'Цель не достигнута. Начинается повтор', k)


# Расчет значений весовых коэффициентов по правилу Хебба (Биполярный нейрон)
def weight_calculation_bipolar(weight, neuron_value, neuron_output):
    neuron_null = 1  # Значение подстроечного нейрона x[0] = 1
    weight[0] += neuron_null * neuron_output  # Значение w[0] = w[0] + x[0] * y
    for i in range(1, len(weight)):
        weight[i] += neuron_value[i - 1] * neuron_output  # w[i] = w[i] + x[i] * y
    return weight  # Возвращаем весовые коэффиценты


# Расчет значений весовых коэффициентов по правилу Хебба (Бинарный нейрон)
def weight_calculation_binary(weight, neuron_value, neuron_output):
    weight[0] += 1 if neuron_output == 1 else -1  # Значение w[0] = w[0] + 1, если (x[0] * y = 1)
    # или w[0] = w[0] - 1, если (x[0] != 0 и y = 0)
    for i in range(1, len(weight)):  # Формула Хебба для бинарного нейрона
        weight_corr_value = 1 if (neuron_value[i - 1] * neuron_output == 1) \
            else -1 if (neuron_value[i - 1] != 0 and neuron_output == 0) else 0
        weight[i] += weight_corr_value
    return weight  # Возвращаем весовые коэффициенты


# Проверка качества обучения
def quality_checking(weight, neuron_value1, neuron_value2):
    # Первое изображение
    total = weight[0]  # Добавляем в сумму w[0]
    for i in range(1, len(weight)):
        total += neuron_value1[i - 1] * weight[i]  # Вычисление суммы S += x[i] * w[i]

    # Второе изображение
    total2 = weight[0]  # Добавляем в сумму w[0]
    for i in range(1, len(weight)):
        total2 += neuron_value2[i - 1] * weight[i]  # Вычисление суммы S += x[i] * w[i]

    # Если полученные вектор равен целевому вектору, то цель достигнута и возвращаем 1
    # Если нет, то возвращаем 0 и выполняем шаги ещё раз
    return 1 if (total > 0 > total2) else 0


bipolarImages = {
    'Тип нейрона': 'Биполярный',
    'Изображение 1': {
        'Значение': [1, -1, 1, 1, 1, 1, -1, -1, 1],  # Начальные данные (Буква Ч)
        'Выходной сигнал': 1,  # Выходной сигнал
    },
    'Изображение 2': {
        'Значение': [1, 1, 1, 1, -1, 1, 1, -1, 1],   # Начальные данные (Буква П)
        'Выходной сигнал': -1,  # Выходной сигнал
    },
}

binaryImages = {
    'Тип нейрона': 'Бинарный',
    'Изображение 1': {
        'Значение': [1, 0, 1, 1, 1, 1, 0, 0, 1],  # Начальные данные (Буква Ч)
        'Выходной сигнал': 1,  # Выходной сигнал
    },
    'Изображение 2': {
        'Значение': [1, 1, 1, 1, 0, 1, 1, 0, 1],   # Начальные данные (Буква П)
        'Выходной сигнал': 0,  # Выходной сигнал
    },
}

print('Выполнение алгоритма Хебба для букв Ч и П (Биполярный нейрон):')
hebbs_rule(bipolarImages)
print('\nВыполнение алгоритма Хебба для букв Ч и П (Бинарный нейрон):')
hebbs_rule(binaryImages)

bipolarImages = {
    'Тип нейрона': 'Биполярный',
    'Изображение 1': {
        'Значение': [1, -1, 1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1],  # Начальные данные (Изображение 1)
        'Выходной сигнал': 1,  # Выходной сигнал
    },
    'Изображение 2': {
        'Значение': [-1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1],  # Начальные данные (Изображение 2)
        'Выходной сигнал': -1,  # Выходной сигнал
    },
}

binaryImages = {
    'Тип нейрона': 'Бинарный',
    'Изображение 1': {
        'Значение': [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],  # Начальные данные (Изображение 1)
        'Выходной сигнал': 1,  # Выходной сигнал
    },
    'Изображение 2': {
        'Значение': [0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],  # Начальные данные (Изображение 2)
        'Выходной сигнал': 0,  # Выходной сигнал
    },
}

print('\nВыполнение алгоритма Хебба для изображений (Биполярный нейрон):')
hebbs_rule(bipolarImages)
print('\nВыполнение алгоритма Хебба для изображений (Бинарный нейрон):')
hebbs_rule(binaryImages)
