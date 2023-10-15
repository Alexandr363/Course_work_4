class Vacancy:
    """Класс для работы с вакансиями"""
    def __init__(self, profession, date_published, salary, link, id_vac):
        self.profession = profession
        self.date_published = date_published
        self.salary = salary
        self.link = link
        self.id_vac = id_vac

    def __repr__(self):
        return (f"- Профессия: {self.profession}\n"
                f"- Дата публикации вакансии: {self.date_published}\n"
                f"- Зарплата: {self.salary}\n"
                f"- Ссылка на вакансию: {self.link}\n"
                f"- ID вакансии: {self.id_vac}\n")
