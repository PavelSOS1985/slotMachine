import random
import os
import time

# глобальные переменные
get_bet = True
bet = None
score = None

# словарь для определения выпадания чисел в определенные столбцы
dict_res = {
    "111": {
        "value": "x",
        "list_col": [0, 3, 6, 9, 12, 15]
    },
    "222": {
        "value": "x",
        "list_col": [0, 3, 6, 9, 12, 15]
    },
    "333": {
        "value": "x",
        "list_col": [0, 3, 6, 9, 12, 15]
    },
    "112": {
        "value": "1",
        "list_col": [0, 3, 12, 15]
    },
    "113": {
        "value": "1",
        "list_col": [0, 3, 12, 15]
    },
    "223": {
        "value": "1",
        "list_col": [0, 3, 12, 15]
    },
    "221": {
        "value": "1",
        "list_col": [3, 6, 9, 12]
    },
    "331": {
        "value": "1",
        "list_col": [3, 6, 9, 12]
    },
    "332": {
        "value": "1",
        "list_col": [3, 6, 9, 12]
    },
    "121": {
        "value": "1",
        "list_col": [6, 9]
    },
    "131": {
        "value": "1",
        "list_col": [6, 9]
    },
    "232": {
        "value": "1",
        "list_col": [6, 9]
    },
    "212": {
        "value": "3",
        "list_col": [0, 3, 12, 15]
    },
    "313": {
        "value": "3",
        "list_col": [0, 3, 12, 15]
    },
    "323": {
        "value": "3",
        "list_col": [0, 3, 12, 15]
    },
    "122": {
        "value": "3",
        "list_col": [0, 6, 9, 15]
    },
    "133": {
        "value": "3",
        "list_col": [0, 6, 9, 15]
    },
    "233": {
        "value": "3",
        "list_col": [0, 6, 9, 15]
    },
    "211": {
        "value": "5",
        "list_col": [0, 3, 12, 15]
    },
    "311": {
        "value": "5",
        "list_col": [0, 3, 12, 15]
    },
    "322": {
        "value": "5",
        "list_col": [0, 3, 12, 15]
    },
    "123": {
        "value": "3",
        "list_col": [0, 15]
    },
    "321": {
        "value": "5",
        "list_col": [3, 12]
    },
    "132": {
        "value": "5",
        "list_col": [6, 9]
    },
    "231": {
        "value": "7",
        "list_col": [6, 9]
    },
    "213": {
        "value": "7",
        "list_col": [3, 12]
    },
    "312": {
        "value": "7",
        "list_col": [0, 15]
    }
}


# функция запроса ставки у пользователя
def _get_bet():
    _bet = None
    while _bet != "0" and _bet != "1" and _bet != "3" and _bet != "5" and _bet != "7":
        # очистка консоли
        os.system('cls')

        print("0 - 50 баллов; ")
        print("1 - 100 баллов; ")
        print("3 - 200 баллов; ")
        print("5 - 500 баллов; ")
        print("7 - 1000 баллов. ")
        _bet = input("Введите ставку: ")
    if _bet == "0":
        _bet = 50
    elif _bet == "1":
        _bet = 100
    elif _bet == "3":
        _bet = 200
    elif _bet == "5":
        _bet = 500
    elif _bet == "7":
        _bet = 1000
    return _bet


print("Приветствуем в игре колесо фортуны!\n")

# просим внести депозит
while score != 50 and score != 100 and score != 200 and score != 500 and score != 1000 and score != 5000:
    try:
        score = int(input("Введите сумму баллов: "))
    except ValueError:
        print("Необходимо ввести целое число 50 | 100 | 200 | 500 | 1000 | 5000 !")

while 1:

    # меняем ставку если надо
    if get_bet:
        bet = _get_bet()
    get_bet = False

    # если ставка больше баланса сообщаем об этом и выходим из игры
    if bet > score:
        print("У вас недостаточно средств!")
        time.sleep(3)
        break

    # очистка консоли
    os.system('cls')

    # играем
    print("Ваша ставка x = " + str(bet))
    score = score - bet

    # создаем игровое поле
    x = 13
    y = 18
    playing_field = []
    for i in range(x):
        playing_field.append([])
        for j in range(y):
            playing_field[i].append(str(random.randint(1, 3)))

    # выполнение первого алгоритма викторины - пункт 3
    for i in range(x):
        str_numbers = ""
        for j in range(0, y, 3):
            str_numbers = playing_field[i][j] + playing_field[i][j + 1] + playing_field[i][j + 2]
            if dict_res.get(str_numbers).get("list_col").count(j) > 0:
                playing_field[i][j] = dict_res.get(str_numbers).get("value")
                playing_field[i][j + 1] = dict_res.get(str_numbers).get("value")
                playing_field[i][j + 2] = dict_res.get(str_numbers).get("value")
            else:
                playing_field[i][j] = "0"
                playing_field[i][j + 1] = "0"
                playing_field[i][j + 2] = "0"

    # заменяем нули на предшествующие
    for i in range(x):
        for j in range(y):
            temp_i = i - 1
            if playing_field[i][j] == "0":
                while playing_field[temp_i][j] == "0":
                    temp_i -= 1
                playing_field[i][j] = playing_field[temp_i][j]

    print()

    # вывод получившегося игрового поля
    for i in range(x):
        for j in range(y):
            print(playing_field[i][j], end=" ")
        print()

    # подсчет выйгрыша
    prize = 0
    for i in range(x):
        temp_num = playing_field[i][0]
        count_nums = 0
        for j in range(3, y, 3):
            if playing_field[i][j] == temp_num:
                count_nums += 1
            else:
                break
        if count_nums > 0 and temp_num == "7":
            prize = prize + count_nums * bet
        if count_nums > 1 and temp_num == "5":
            prize = prize + (count_nums - 1) * bet
        if count_nums > 2 and temp_num == "3":
            prize = prize + (count_nums - 2) * bet
        if count_nums > 3 and temp_num == "1":
            prize = prize + (count_nums - 3) * bet
        if count_nums > 4 and temp_num == "x":
            prize = prize + (count_nums - 4) * bet
    score += prize

    print()
    print("Ваш баланс: " + str(score))
    print("Выйгрыш: " + str(prize))
    print()

    # меню игры
    print("Введите b (bet) если хотите изменить ставку")
    print("Введите r (repeat) если хотите повторить")
    print("Введите e (exit) для выхода")
    menu_choice = None
    while menu_choice != "b" and menu_choice != "r" and menu_choice != "e":
        menu_choice = str(input("Ваш выбор: "))
    print()

    if menu_choice == "b":
        get_bet = True
    elif menu_choice == "r":
        continue
    else:
        print("Спасибо за игру")
        time.sleep(3)
        break
