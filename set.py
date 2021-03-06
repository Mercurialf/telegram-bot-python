import sqlite3

# Соединения
conn = sqlite3.connect('list.db')
# Запросы-хранение
cur = conn.cursor()

# Таблица
cur.execute("""CREATE TABLE IF NOT EXISTS greetings(
    id INT PRIMARY KEY,
    main TEXT);
""")
conn.commit()

# Таблица
cur.execute("""CREATE TABLE IF NOT EXISTS advice(
    id INT PRIMARY KEY,
    main TEXT);
""")
conn.commit()

greetings_list = [
    ('001', 'Привет'), ('002', 'привет'),
    ('003', 'ПРИВЕТ'), ('004', 'пРИВЕТ'),
    ('005', 'Привет!'), ('006', 'Привет?')
]

advice_list = [
    ('1', 'Первый Текст'), ('2', 'Второй Текст'), ('3', 'Третий Текст'),
    ('4', 'Четвертый Текст'), ('5', 'Пятый текст'), ('6', 'Шестой текст')
]

# Добавление данных в таблицу:
cur.executemany("INSERT INTO greetings VALUES(?, ?);", greetings_list)
cur.executemany("INSERT INTO advice VALUES(?, ?);", advice_list)


advice_list = ['Самые вкусные котлеты получатся из фарша, который постоит 5-6 часов вместе с нарезанным луком, '
               'солью и специями в холодильнике. Мясо немного замаринуется, котлеты будут гораздо вкуснее!',
               'Горячее молоко с кардамоном — напиток, который быстро поможет снять воспаление, '
               'если начинает болеть горло.',
               'Если нужно быстро разжечь костер, вспомните о чипсах. Они горят лучше, чем любая специальная жидкость, '
               'и отлично работают даже с сырыми дровами!',
               'Место ожога будет болеть не так сильно и неприятные ощущения пройдут быстрее, '
               'если смазать поврежденный участок кожи зубной пастой.']


# Список запросов от пользователя
main_list = ['Привет', 'привет', 'ПРИВЕТ', 'пРИВЕТ', 'Привет!']
rand_list = ['Бот, да или нет?', 'Да или нет?', 'да или нет?']

# Список ответов для бота
main_answer_list = ['Привет!', 'Здравствуй!']
answer_rand_list = ['Да!', 'Нет!']

weather_list = ['Погода Киев', 'Погода Харьков', 'Погода Одесса', 'Погода Днепр',
                'Погода Донецк',
                'Погода Запорожье', 'Погода Львов', 'Погода Кривой Рог', 'Погода Николаев',
                'Погода Севастополь', 'Погода Мариуполь', 'Погода Луганск', 'Погода Винница',
                'Погода Симферополь', 'Погода Макеевка', 'Погода Херсон', 'Погода Чернигов',
                'Погода Полтава', 'Погода Черкассы', 'Погода Хмельницкий', 'Погода Черновцы',
                'Погода Житомир', 'ПогодаСумы', 'Погода Ровно', 'Погода Горловка', 'Погода Ивано-Франковск',
                'Погода Каменское', 'Погода Кропивницкий', 'Погода Тернополь', 'Погода Кременчуг',
                'Погода Луцк', 'Погода Белая Церковь', 'Погода Краматорск', 'Погода Мелитополь',
                'Погода Керчь', 'Погода Ужгород', 'Погода Бердянск', 'Погода Никополь', 'Погода Славянск',
                'Погода Евпатория', 'Погода Бровары', 'Погода Алчевск', 'Погода Павлоград',
                'Погода Северодонецк', 'Погода Варшава']

currency_list_usd = ['USD', 'usd']
currency_list_pln = ['PLN', 'pln']
