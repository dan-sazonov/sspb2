import os

import psycopg2
from psycopg2 import Error

usr = os.getenv('DB_TEST_USR')
pas = os.getenv('DB_TEST_PASS')

try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user=usr,
                                  # пароль, который указали при установке PostgreSQL
                                  password=pas,
                                  host="127.0.0.1",
                                  port="5432",
                                  database="sspb2")

    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # Распечатать сведения о PostgreSQL
    print("Информация о сервере PostgreSQL")
    print(connection.get_dsn_parameters(), "\n")
    # Выполнение SQL-запроса
    cursor.execute("SELECT version();")
    # Получить результат
    record = cursor.fetchone()
    print("Вы подключены к - ", record, "\n")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
input()
