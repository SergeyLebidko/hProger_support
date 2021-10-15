import json
from sys import platform

PATH = r'C:\Users\User\PycharmProjects\hungry_proger\src\content\\'
if platform == 'linux':
    PATH = r'/home/sergey/PycharmProjects/hungry_proger/src/content/'

OUTPUT_FILE = 'data.json'

# Данные для раздела с перечнем скиллов
skills_data = [
    {
        'title': 'JavaScript',
        'tech': ('React', 'Redux', 'Thunk', 'React Router', 'jQuery')
    },
    {
        'title': 'Python',
        'tech': ('Django', 'Django Rest Framework', 'pygame')
    },
    {
        'title': 'HTML/CSS',
        'tech': ('Семантическая верстка', 'Технология БЭМ', 'SCSS', 'Flexbox-верстка')
    }
]

# Данные для раздела с перечнем проектов
projects_data = [
    {
        'git': 'https://github.com/SergeyLebidko/Abalone',
        'title': 'Abalone',
        'description': 'Реализация настольной игры "Абалон", созданной французскими игровыми дизайнерами в 1987 году.',
        'tech': ('Python', 'pygame')
    },
    {
        'git': 'https://github.com/SergeyLebidko/graphite_client',
        'title': 'Graphite',
        'description': 'Платформа для ведения блогов. Мой первый проект, в котором фронтэнд написан полностью на React',
        'tech': ('Python', 'Django', 'DRF', 'React', 'CSS')
    },
    {
        'git': 'https://github.com/SergeyLebidko/MiniStorage',
        'title': 'MiniStorage',
        'description': 'Простая система ведения учета на небольшом складе с базовым набором возможностей',
        'tech': ('DRF', 'JavaScript', 'jQuery', 'CSS', 'Python', 'Django')
    },
    {
        'git': 'https://github.com/SergeyLebidko/Hexagon',
        'title': 'Hexagon',
        'description': 'Игра-пазл на поле из гексов',
        'tech': ('Python', 'pygame')
    },
    {
        'git': 'https://github.com/SergeyLebidko/hungry_proger',
        'title': 'hProger',
        'description': 'Сайт, на котором вы сейчас находитесь. Можете кликнуть на логотип github\'a в углу карточки и посмотреть его исходный код :)',
        'tech': ('React', 'paper.js', 'CSS', 'SCSS')
    },
    {
        'git': 'https://github.com/SergeyLebidko/PyChess',
        'title': 'PyChess',
        'description': 'Шахматы на Python. Один из первых моих проектов на этом языке',
        'tech': ('Python', 'pygame')
    },
    {
        'git': 'https://github.com/SergeyLebidko/LiteInventory',
        'title': 'LiteInventory',
        'description': 'Небольшой сервис для учета компьютерной и оргтехники',
        'tech': ('Python', 'Django', 'DRF')
    },
    {
        'git': 'https://github.com/SergeyLebidko/soccer_stat',
        'title': 'Soccer Stat',
        'description': 'Небольшой сервис для просмотра футбольной статистики, основанный на бесплатном API сайта www.football-data.org',
        'tech': ('React', 'HTML', 'CSS')
    },
    {
        'git': 'https://github.com/SergeyLebidko/need_for_drive',
        'title': 'Need for drive',
        'description': 'Сайт для сервиса каршеринга, разработанный в рамках практикума в компании SimbirSoft',
        'tech': ('React', 'Redux', 'React Router')
    },
    {
        'git': 'https://github.com/SergeyLebidko/need_for_drive_admin',
        'title': 'NFD Admin',
        'description': 'Административная панель для сервиса каршеринга, разработанная в рамках практикума в компании SimbirSoft',
        'tech': ('React', 'Redux', 'React Router')
    }
]


def main():
    to_file = {
        'skills': skills_data,
        'projects': projects_data
    }
    with open(PATH + OUTPUT_FILE, 'wt') as output_file:
        output_file.write(json.dumps(to_file, indent=2, sort_keys=False, ensure_ascii=False))

    print('Запись завершена...')


if __name__ == '__main__':
    main()
