import psycopg2


def db_connect():
    database = psycopg2.connect(
        dbname='weather',
        host='localhost',
        user='postgres',
        password='123456'
    )
    return database


def create_table():
    database = db_connect()
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS translate_history(
        history_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        chat_id BIGINT,
        city_name VARCHAR(30),
        text VARCHAR
    );
    ''')

    database.commit()
    database.close()


create_table()


def create_bot_table():
    database = db_connect()
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bot(
        bot_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        bot_name VARCHAR(30),
        bot_token VARCHAR
    );    
    ''')

    database.commit()
    database.close()


create_bot_table()


def get_token():
    database = db_connect()
    cursor = database.cursor()
    cursor.execute('''
    SELECT bot_token FROM bot WHERE bot_name = %s 
    ''', ('translate',))
    token = cursor.fetchone()
    database.close()
    return token[0]


def db_history_write(chat_id, city_name, text):
    database = db_connect()
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO translate_history(chat_id, city_name, text)
    VALUES (%s, %s, %s) ''', (chat_id, city_name, text))
    database.commit()
    database.close()


def db_history_read(chat_id):
    database = db_connect()
    cursor = database.cursor()
    cursor.execute('''SELECT city_name, text 
    FROM translate_history
    WHERE chat_id = %s ''', (chat_id,))
    history = cursor.fetchall()
    history = history[::-1]
    database.close()
    return history
