def taxi_distribution(N, distances, tariffs):
    total_cost = 0
    taxi_assignment = []

    # Сортировка расстояний и тарифов по возрастанию
    sorted_distances = sorted(enumerate(distances), key=lambda x: x[1])
    sorted_tariffs = sorted(enumerate(tariffs), reverse= True, key=lambda x: x[1])

    # Распределение сотрудников по такси с минимальными затратами
    for i in range(N):
        employee_index = sorted_distances[i][0]
        taxi_index = sorted_tariffs[i][0]
        cost = sorted_distances[i][1] * sorted_tariffs[i][1]
        total_cost += cost
        taxi_assignment.append(taxi_index + 1)  # +1 для номерации такси с 1

    return total_cost, taxi_assignment

#Вывод суммы словами (из одной из предыдущих лабораторных работ, с заменой num на total_cost )
def total_cost_to_words(total_cost):
    if total_cost < 0 or total_cost > 100000:
        print("Число должно быть от 1 до 100000")
    else:
        num_words = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять",
                     "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать",
                     "семнадцать", "восемнадцать", "девятнадцать"]
        tens_words = ["двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
                      "девяносто"]
        hundreds_words = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот",
                          "девятьсот"]
        thousands_words = ["тысяч"]
        rubles_words = ["рубл"]

        # определяем разряды числа
        units = total_cost % 10  # единицы
        tens = (total_cost // 10) % 10  # десятки
        hundreds = (total_cost // 100) % 10  # сотни
        thousands = total_cost // 1000  # тысячи
        thousands1 = total_cost // 10000%10
        # определяем порядок числа
        order = ""
        if thousands > 0:
            order = "тысяч"
            if thousands == 1:
                order = "тысяч"
            elif thousands >= 2 and thousands <= 4:
                order = "тысяч"
        elif total_cost == 0:
            order = "рублей"

        # определяем окончание для рублей
        rubles_end = ""
        if units == 1 and tens != 1:
            rubles_end = "ь"
        elif units >= 2 and units <= 4 and tens != 1:
            rubles_end = "я"
        else:
            rubles_end = "ей"

        # определяем окончание для тысяч
        thousands_end = ""
        if thousands == 1 :
            thousands_end = "а"
        elif thousands >= 2 and thousands <= 4:
            thousands_end = "и"

        # формируем словесное представление числа
        total_cost_in_words = ""
        if total_cost == 0:
            num_in_words = "Ошибка! Число должно быть от 1 до 100000."
        else:
            if thousands == 1 :
                total_cost_in_words += "одна тысяч" + thousands_end + " "
            if thousands == 2 :
                total_cost_in_words += "две тысяч" + thousands_end + " "  
            if thousands > 2 :
                if thousands < 20 :
                    total_cost_in_words += num_words[thousands] + " " + order + thousands_end + " "
                else:
                    total_cost_in_words += tens_words[total_cost//10000-2] + " " + num_words[num//1000%10] + " " + order + thousands_end + " "
            if hundreds > 0:
                total_cost_in_words += hundreds_words[hundreds - 1] + " "
            if tens > 1:
                total_cost_in_words += tens_words[tens - 2] + " "
            if tens == 1:
                total_cost_in_words += num_words[total_cost % 100] + " "
            elif units > 0:
                total_cost_in_words += num_words[units] + " "
            total_cost_in_words += rubles_words[0] + rubles_end

        # выводим результат
        print('Сумма затрат:', total_cost_in_words)
def main():
    # Ввод количества сотрудников
    N = int(input("Введите количество сотрудников: "))
    if N >= 1000  :
        print ("Количество сотрудников не может превышать 1000")
    if  N <= 1 :
        print ("Количество сотрудников не может быть отрицательным числом")

    # Ввод расстояний от работы до домов сотрудников
    distances = []
    for i in range(N):
        distance = int(input(f"Введите расстояние для {i+1}-го сотрудника в км: "))
        distances.append(distance)

    # Ввод тарифов за проезд в такси
    tariffs = []
    for i in range(N):
        tariff = int(input(f"Введите тариф для {i+1}-го такси в рублях: "))
        tariffs.append(tariff)

    # Расчет распределения сотрудников по такси с минимальными затратами
    total_cost, taxi_assignment = taxi_distribution(N, distances, tariffs)

    # Вывод распределения сотрудников по такси
    print("Распределение сотрудников по такси:")
    for i, taxi in enumerate(taxi_assignment):
        print(f"Сотрудник {i+1} -> Такси {taxi}")

    # Вывод суммы затрат в рублях
    print("Сумма затрат:", total_cost, "рублей")

    # Форматирование суммы затрат словами
    formatted_cost = total_cost_to_words(total_cost)
if __name__ == "__main__":
    main()