"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(string_1, string_2):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    if isinstance(string_1, str) and isinstance(string_2, str):
        if string_1 == string_2:
            print (1)
        elif len(string_1) > len(string_2) and string_2 != 'learn':
            print (2)
        elif string_1 != string_2 and string_2 == 'learn':
            print (3)
    else:
        print (0)
    
if __name__ == "__main__":
    string_1 = ''
    string_2 = 3
    string_3 = 1
    string_4 = 'a'
    string_5 = 'aa'
    string_6 = 'aa'
    string_7 = 'python'
    string_8 = 'aa'
    string_9 = 'python'
    string_10 = 'learn'
    main(string_1, string_2)
    main(string_3, string_4)
    main(string_5, string_6)
    main(string_7, string_8)
    main(string_9, string_10)
