from abc import ABC, abstractmethod
import json
from pathlib import Path


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

    USER_PATH = "user.json"

    def __new__(cls, *args, **kwargs):
        """Создание файла для выборки пользователя
        по вакансиям, если файл не существует."""
        if not Path(cls.USER_PATH).resolve().exists():
            with open(cls.USER_PATH, "w"):
                pass
        return super().__new__(cls)

    def save_vacancy(self, id_vac):
        with open('data.json', encoding='utf-8') as d:
            data_dict = json.load(d)

        with open(self.USER_PATH, encoding='utf-8') as u:
            try:
                user_dict = json.load(u)
            except json.decoder.JSONDecodeError:
                user_dict = {}

        with open(self.USER_PATH, 'w', encoding='utf-8') as u:
            json.dump(user_dict | {id_vac: data_dict[id_vac]}, u, indent=2,
                      ensure_ascii=False)

    def delete_vacancy(self, id_vac):

        with open(self.USER_PATH, encoding='utf-8') as f:
            data = json.load(f)
            try:
                del data[id_vac]
                print("Вакансия удалена")
            except KeyError:
                print("Такой вакансии нет")
                pass

        with open(self.USER_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def get_vacancy(self, id_vac):
        with open(self.USER_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(data[id_vac])
