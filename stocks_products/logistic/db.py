import sqlite3

# Создайте или откройте существующую базу данных
conn = sqlite3.connect('db')

# Выполните коммит изменений
conn.commit()

# Закройте соединение с базой данных
conn.close()
