# Задача: Наибольшие числа
# Считываем количество чисел в последовательности[span_1](start_span)[span_1](end_span)
n = int(input())

# Инициализируем переменные для хранения первого и второго максимума[span_2](start_span)[span_2](end_span)
largest = 0
largest_2 = 0

# Обрабатываем каждое введённое число[span_3](start_span)[span_3](end_span)
for i in range(1, n + 1):
    k = int(input())
    
    # Если новое число больше главного максимума:
    # Сначала сохраняем старый максимум во вторую переменную, затем обновляем главный[span_4](start_span)[span_4](end_span)
    if largest < k:
        largest_2 = largest
        largest = k
        
    # Если новое число меньше главного максимума, но больше второго[span_5](start_span)[span_5](end_span)
    elif largest > k > largest_2:
        largest_2 = k

# Выводим два самых больших числа[span_6](start_span)[span_6](end_span)
print(largest, largest_2, sep='\n')