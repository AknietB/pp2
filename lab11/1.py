import psycopg2, csv, ast

# Подключение к БД
db = psycopg2.connect(
    dbname='ernar',
    user='postgres',
    password='akniet07',
    host='localhost',
    port='5432'
)

current = db.cursor()

print(''' What do you want?
"1" Add or update contact
"2" Add contacts from .csv file
"3" Search by pattern
"4" Show first N contacts
"5" Show all phone numbers
"6" Change name or phone
"7" Add many contacts from list (with validation)
"8" Show contacts with pagination (LIMIT + OFFSET)
"9" Delete contact by name or phone
"0" Show whole phonebook
''')

req = input("Enter the number: ")

# 1. Вставка или обновление
if req == '1':
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    current.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
    print("Inserted or updated.")

# 2. Импорт из CSV
elif req == '2':
    path = input("Enter CSV path: ")
    with open(path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            current.execute("CALL insert_or_update_user(%s, %s);", (row[0], row[1]))
    print("Contacts from CSV added.")

# 3. Поиск по шаблону
elif req == '3':
    pattern = input("Enter pattern to search: ")
    current.execute("SELECT * FROM search_contacts(%s);", (pattern,))
    for row in current.fetchall():
        print(row)

# 4. Первые N контактов
elif req == '4':
    n = int(input("Enter number of contacts: "))
    current.execute("SELECT * FROM get_contacts_with_pagination(%s, %s);", (n, 0))
    for row in current.fetchall():
        print(row)

# 5. Только телефоны
elif req == '5':
    current.execute("SELECT phone_number FROM phonebook;")
    for row in current.fetchall():
        print(row[0])

# 6. Изменение имени или номера
elif req == '6':
    choice = input("What to update (name/phone)? ")
    if choice == 'name':
        phone = input("Enter current phone: ")
        new_name = input("Enter new name: ")
        current.execute("UPDATE phonebook SET person_name = %s WHERE phone_number = %s;", (new_name, phone))
    elif choice == 'phone':
        name = input("Enter current name: ")
        new_phone = input("Enter new phone: ")
        current.execute("UPDATE phonebook SET phone_number = %s WHERE person_name = %s;", (new_phone, name))
    print("Updated successfully.")

# 7. Множественная вставка с проверкой
elif req == '7':
    raw = input("Enter list of tuples [(name, phone), ...]: ")
    contact_list = ast.literal_eval(raw)  # осторожно: проверяй ввод
    # преобразуем в массив массивов (для PostgreSQL TEXT[][])
    arr = [[x[0], x[1]] for x in contact_list]
    current.execute("CALL insert_many_users(%s);", (arr,))
    print("Batch insert completed (check DB for results).")

# 8. Пагинация
elif req == '8':
    page = int(input("Enter page number: "))
    size = int(input("Enter page size: "))
    offset = (page - 1) * size
    current.execute("SELECT * FROM get_contacts_with_pagination(%s, %s);", (size, offset))
    result = current.fetchall()
    for row in result:
        print(row)

# 9. Удаление
elif req == '9':
    info = input("Enter name or phone to delete: ")
    current.execute("CALL delete_contact(%s);", (info,))
    print("Deleted successfully.")

# 0. Показать всё
elif req == '0':
    current.execute("SELECT * FROM phonebook;")
    results = current.fetchall()
    print("PHONEBOOK")
    print("==========================================")
    print("NAME                PHONE")
    print("==========================================")
    for row in results:
        print('{0:20}{1:20}'.format(row[0], row[1]))

else:
    print("Unknown option.")

current.close()
db.commit()
db.close()