import mysql.connector

# Функция для регистрации пользователя
def register_user(username, password):
    # Подключаемся к базе данных
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='~gZviBgh4AcOaK*3k$WP',
        database='users'  # Имя вашей базы данных
    )
    cursor = connection.cursor()

    # Вставляем нового пользователя в базу данных
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    connection.commit()

    # Закрываем соединение с базой данных
    cursor.close()
    connection.close()
