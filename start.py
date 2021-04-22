import json

PATH = r'C:\Users\User\PycharmProjects\hungry_proger\public\content\\'
GIT_URL = 'https://github.com/SergeyLebidko/'


def read_content(filename):
    with open(filename, encoding='utf-8') as file:
        paragraph_list = []
        for line in file.read().split('*'):
            paragraph_list.append(line)

    return paragraph_list


def save_data(data, filename):
    with open(PATH + filename + '.txt', 'wt', encoding='utf-8') as file:
        file.write(json.dumps(data, ensure_ascii=False))


# Создаем файл "Обо мне"
header = read_content('about_me_header.txt')
body = read_content('about_me_body.txt')
save_data({'header': header, 'body': body}, 'about_me')

# Создаем файл с перечнем проектов
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
        ('React', 'paper.js', 'Axios', 'CSS', 'SCSS')
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

save_data(data_list, 'projects')

# Готовим данные о скиллах
data_list = ['Python', 'Django', 'JavaScript', 'jQuery', 'React', 'HTML', 'CSS']
save_data(data_list, 'skills')

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

save_data(data_list, 'contacts')

# Готовим подробные данные о скиллах
header = read_content('skills_detail_header.txt')
body = read_content('skills_detail_body.txt')
save_data({'header': header, 'body': body}, 'skills_detail')