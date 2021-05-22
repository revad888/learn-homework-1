"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
import random
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school = []
    all_school_score = []
    for school_class in range(1, 12):
        classes = ['а', 'б']
        for i in classes:
            cl = str(school_class) + i
            scores = []
            for score in range(5):
                scores.append(random.randint(1,5))
            school.append({'school_class': cl, 'scores': scores})
    for some_class in school:
        for score in some_class['scores']:
            all_school_score.append(score)
    school_awg = round(sum(all_school_score)/len(all_school_score), 1)
    print (f'Средний бал по школе: {school_awg}')
    for some_class in school:
        class_number = some_class['school_class']
        class_scores = some_class['scores']
        class_awg = round(sum(class_scores) / len(class_scores), 2)
        print (f'Средний бал класса {class_number}: {class_awg}')

        



    
if __name__ == "__main__":
    main()
