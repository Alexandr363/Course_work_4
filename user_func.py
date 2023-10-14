import json
from api_class import SuperJobAPI, HeadHunterAPI
from utils import good_view, good_view_2


def user_input():
    """Функция для взаимодействия с пользователем, делает запрос к API,
       сохраняет результат в data.json и выводит на экран"""

    sj_api = SuperJobAPI()
    hh_api = HeadHunterAPI()
    format_result = None

    print('1 - Super Job   2 - HeadHunter   3 - оба')
    while True:
        website = input('Введите, с какого сайта искать вакансии: '
                        '(число от 1 до 3) \n')
        if website.isdigit():
            if 4 > int(website) > 0:
                break

    while True:
        vacancy_count = input('Введите количество вакансий для поиска: '
                              '(число от 1 до 99) \n')
        if vacancy_count.isdigit():
            if 100 > int(vacancy_count) > 0:
                break

    while True:
        search_phrase = input('Введите ключевое слово для поиска: '
                              '(без цифр) \n')
        if search_phrase.isalpha():
            break

    if int(website) == 1:
        result = sj_api.get_vacancies(search_phrase, vacancy_count)
        format_result = sj_api.format_data(result)
    elif int(website) == 2:
        result = hh_api.get_vacancies(search_phrase, vacancy_count)
        format_result = hh_api.format_data(result)
    elif int(website) == 3:
        result_1 = sj_api.get_vacancies(search_phrase, vacancy_count)
        result_2 = hh_api.get_vacancies(search_phrase, vacancy_count)
        a = sj_api.format_data(result_1)
        b = hh_api.format_data(result_2)
        format_result = a | b

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(format_result, f, indent=2, ensure_ascii=False)
    print()
    a = good_view(format_result)
    good_view_2(a)
