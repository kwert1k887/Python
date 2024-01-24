import pymysql

connection = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='',
    database='apps'
)

try:
    print("База данных успешно подключена.")
except Exception as ex:
    print(f"Ошибка: {ex}")