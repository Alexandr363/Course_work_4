from abc import ABC, abstractmethod
import os
import requests
from utils import unix_time, iso_time


class GetApi(ABC):
    """Абстрактный класс для вакансий"""
    @abstractmethod
    def get_vacancies(self, search_phrase: str, count: int):
        pass

    @abstractmethod
    def format_data(self, response):
        """Приводим данные к единому виду """
        pass


class HeadHunterAPI(GetApi):
    """Класс для получения вакансий с Head Hunter"""

    def get_vacancies(self, search_phrase: str, count: str):
        """Запрашиваем вакансии с Head Hunter"""
        url = 'https://api.hh.ru/vacancies'
        response = requests.get(url, params={'text': search_phrase,
                                             'per_page': count})
        if response.status_code == 200:
            return response.json()

    def format_data(self, response):
        """Приводим данные к единому виду"""
        data = {}
        for v in response['items']:
            vac_id = v['id']
            if v['salary'] is None:
                v['salary'] = ''
            else:
                if v['salary']['from'] is None:
                    salary_from = ''
                else:
                    salary_from = v['salary']['from']
                if v['salary']['to'] is None:
                    salary_to = ''
                else:
                    salary_to = v['salary']['to']
                data[vac_id] = {'profession': v['name'],
                                'date_published': iso_time(v['published_at']),
                                'salary': f"от {salary_from} до {salary_to}"
                                          f" {v['salary']['currency']}",
                                'link': v['alternate_url'],
                                'id': v['id']
                                }
        return data


class SuperJobAPI(GetApi):
    """Класс для получения вакансий с Super Job"""

    def get_vacancies(self, search_phrase: str, count: str):
        """Запрашиваем вакансии с Head Hunter"""

        api_key: str = os.getenv('SJ_API_KEY')

        api_url = 'https://api.superjob.ru/2.33/vacancies/'
        params = {'keyword': search_phrase, 'count': count}
        headers = {'X-Api-App-Id': api_key, }
        response = requests.get(api_url, params=params, headers=headers)

        if response.status_code == 200:
            return response.json()

    def format_data(self, response):
        """Приводим данные к единому виду"""
        data = {}
        for v in response['objects']:
            vac_id = v['id']
            data[vac_id] = {'profession': v['profession'],
                            'date_published': unix_time(v['date_published']),
                            'salary': f"{v['payment_from']} - {v['payment_to']}"
                                      f" {v['currency']}",
                            'link': v['link'],
                            'id': v['id']
                            }
        return data
