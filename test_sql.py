import sqlite3

conn = sqlite3.connect(":memory:") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

# Создание таблицы
for sql in open('create_tables.sql').read().split(';'):
    print(sql)
    cursor.execute(sql)