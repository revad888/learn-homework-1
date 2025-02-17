"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main(user_age):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    try:
        age = int(user_age)
        if age <= 0:
            return 'Введите корректное значение'
        elif 0 < age <= 6:
            return 'Вы ходите в детский сад'
        elif 6 < age <=17:
            return 'Вы учитесь в школе'
        elif 17 < age <= 24:
            return 'Вы учитесь в ВУЗе'
        else:
            return 'Вы работаете'
    except ValueError:
        return 'Введите числовое значение'    


if __name__ == "__main__":
    user_age = input('Введите ваш возраст: ')
    
    age = main(user_age)

    print(age)
