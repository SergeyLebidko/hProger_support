import json

PATH = r'C:\Users\User\PycharmProjects\hungry_proger\src\\'
OUTPUT_FILE = 'content.js'
GIT_URL = 'https://github.com/SergeyLebidko/'


# Функция для чтения файлов-исходников
def read_content(filename):
    with open(filename, encoding='utf-8') as file:
        paragraph_list = []
        for line in file.read().split('*'):
            paragraph_list.append(line)

    return paragraph_list


# Функция для записи данных в целевой каталог
def save_data(data):
    with open(PATH + OUTPUT_FILE, 'wt', encoding='utf-8') as file:
        for number, element in enumerate(data):
            if number:
                file.write('\n\n')
            file.write(f'export const {element["literal"]} = ' + json.dumps(element['data'], indent=2, sort_keys=False,
                                                                            ensure_ascii=False))


to_write_data = []

# Готовим данные для раздела "Обо мне"
header = read_content('about_me_header.txt')
body = read_content('about_me_body.txt')
to_write_data.append({
    'literal': 'aboutMe',
    'data': {'header': header, 'body': body}
})

# Готовим данные для раздела с перечнем проектов
projects_data = [
    (
        'Abalone',
        'Abalone',
        'Реализация настольной игры "Абалон", созданной французскими игровыми дизайнерами в 1987 году.',
        ('Python', 'pygame')
    ),
    (
        'graphite_client',
        'Graphite',
        'Платформа для ведения блогов. Мой первый проект, в котором фронтэнд написан полностью на React',
        ('Python', 'Django', 'DRF', 'React', 'CSS')
    ),
    (
        'MiniStorage',
        'MiniStorage',
        'Простая система ведения учета на небольшом складе с базовым набором возможностей',
        ('DRF', 'JavaScript', 'jQuery', 'CSS', 'Python', 'Django')
    ),
    (
        'Hexagon',
        'Hexagon',
        'Игра-пазл на поле из гексов',
        ('Python', 'pygame')
    ),
    (
        'hungry_proger',
        'hProger',
        'Сайт, на котором вы сейчас находитесь. Можете кликнуть на логотип github\'a в углу карточки и посмотреть его исходный код :)',
        ('React', 'paper.js', 'CSS', 'SCSS')
    ),
    (
        'PyChess',
        'PyChess',
        'Шахматы на Python. Один из первых моих проектов на этом языке',
        ('Python', 'pygame')
    ),
    (
        'ReactTraining',
        'ReactTraining',
        'Учебный проект, в котором я обкатывал навыки создания различных React-компонетов и работы с CSS',
        ('Python', 'Django', 'React', 'CSS')
    ),
    (
        'WhiteLinen',
        'WhiteLinen',
        'Проект простого сайта-визитки для небольшой дизайн-студии. Мой первый опыт в верстке лендинга',
        ('HTML', 'CSS', 'jQuery')
    )
]

data_list = []
for git_name, title, description, tech_list in projects_data:
    data_list.append({
        'git': GIT_URL + git_name,
        'title': title,
        'description': description,
        'tech_list': tech_list
    })
to_write_data.append({
    'literal': 'projects',
    'data': data_list
})

# Готовим данные о скиллах
data_list = ['Python', 'Django', 'JavaScript', 'jQuery', 'React', 'HTML', 'CSS']
to_write_data.append({
    'literal': 'skills',
    'data': data_list
})

# Готовим данные о контактах
contacts_data = [
    ('https://github.com/SergeyLebidko', 'git_logo'),
    ('tg://resolve?domain=@sergeyler', 'telegram_logo'),
    ('https://krasnodar.hh.ru/resume/7a068d12ff072536a70039ed1f514b58767550', 'hh_logo'),
    ('mailto:sergeyler@gmail.com', 'email_logo')
]

data_list = []
for url, logo in contacts_data:
    data_list.append({
        'url': url,
        'logo': logo + '.png'
    })
to_write_data.append({
    'literal': 'contacts',
    'data': data_list
})

# Готовим подробные данные о скиллах
header = read_content('skills_detail_header.txt')
body = read_content('skills_detail_body.txt')
to_write_data.append({
    'literal': 'skillsDetail',
    'data': {'header': header, 'body': body}
})

# Сбрасываем данные на диск
save_data(to_write_data)
