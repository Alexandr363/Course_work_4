from work_with_vacancy import AddLoadGet


def save_load_get():
    """Сохраняет/удаляет/выгружает вакансии из файла user.json"""

    action = AddLoadGet()

    print('1 - Сохранить вакансию \n' 
          '2 - Удалить вакансию \n' 
          '3 - Получить вакансию \n'
          '4 - Выход')
    while True:
        user_input = int(input())
        if user_input == 4:
            break
        if user_input == 1:
            vac_id = input('Введите id вакансии:  ')
            action.save_vacancy(vac_id)
        if user_input == 2:
            vac_id = input('Введите id вакансии:  ')
            action.delete_vacancy(vac_id)
        if user_input == 3:
            vac_id = input('Введите id вакансии:  ')
            action.get_vacancy(vac_id)
