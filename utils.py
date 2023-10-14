import datetime
from vacancy import Vacancy


def unix_time(time):
    """Переводит время формата unixtime в datetime"""

    new_time = datetime.datetime.fromtimestamp(time)
    return new_time.strftime('%d.%m.%Y')


def iso_time(time):
    """Переводит время формата iso 8601 в datetime"""

    new_time = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S+%f")
    return new_time.strftime('%d.%m.%Y')


def good_view(data: dict):
    """Принимает словарь вакансий и формирует из него список экземпляров класса
       Vacancy"""

    vacancy = []
    for key, value in data.items():
        vacancy.append(Vacancy(value['profession'],
                               value['date_published'],
                               value['salary'],
                               value['link'],
                               value['id']))
    return vacancy


def good_view_2(data: list):
    """Принимает список экземпляров класса Vacancy и печатает его в удобном
       формате"""

    i = 1
    for dat in data:
        print(i, 60 * '*')
        print(dat)
        i += 1


def new():
    pass
