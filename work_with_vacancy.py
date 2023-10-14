from abc import ABC, abstractmethod
import json


class WorkVacancy(ABC):
    """Абстрактный класс для сохранения, загрузки, запроса вакансий"""

    @abstractmethod
    def save_vacancy(self, id_vac):
        pass

    @abstractmethod
    def delete_vacancy(self, id_vac):
        pass

    @ abstractmethod
    def get_vacancy(self, id_vac):
        pass


class AddLoadGet(WorkVacancy):
    """Класс для сохранения, загрузки, запроса вакансий"""

    def save_vacancy(self, id_vac):

        with open('data.json', encoding='utf-8') as d:
            data_dict = json.load(d)

        with open('user.json', encoding='utf-8') as u:
            user_dict = json.load(u)

        with open('user.json', 'w', encoding='utf-8') as u:
            json.dump(user_dict | {id_vac: data_dict[id_vac]}, u, indent=2,
                      ensure_ascii=False)

    def delete_vacancy(self, id_vac):

        with open('user.json', encoding='utf-8') as f:
            data = json.load(f)
            del data[id_vac]

        with open('user.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def get_vacancy(self, id_vac):
        with open('user.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(data[id_vac])
