import json

from work_with_vacancy import AddLoadGet


def save_load_get():
    """Сохраняет/удаляет/выгружает вакансии из файла self.USER_PATH"""

    action = AddLoadGet()

    while True:
        print('1 - Сохранить вакансию \n'
              '2 - Удалить вакансию \n'
              '3 - Получить вакансию \n'
              '4 - Выход')

        user_input = int(input().strip())

        if user_input == 4:
            break
        else:
            if user_input == 1:
                try:
                    vac_id = input('Введите id вакансии: ')
                    action.save_vacancy(vac_id)
                except KeyError:
                    print('Вы неверно ввели ID вакансии')
            if user_input == 2:
                try:
                    vac_id = input('Введите id вакансии: ')
                    action.delete_vacancy(vac_id)
                except json.decoder.JSONDecodeError:
                    print('Вы неверно ввели ID вакансии')
            if user_input == 3:
                try:
                    vac_id = input('Введите id вакансии: ')
                    action.get_vacancy(vac_id)
                except KeyError:
                    print('Вы неверно ввели ID вакансии')
