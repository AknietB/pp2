import psycopg2
import csv

DB_NAME = "ernar"
DB_USER = "postgres"
DB_PASSWORD = "akniet07"
TABLE_NAME = "phone_numbers"


def get_connection():
    return psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)


def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            phone VARCHAR(20)
        );
    """)
    conn.commit()
    cur.close()
    conn.close()


def insert_from_csv(file_path):
    conn = get_connection()
    cur = conn.cursor()
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader) 
        for row in reader:
            cur.execute(
                f"INSERT INTO {TABLE_NAME} (first_name, last_name, phone) VALUES (%s, %s, %s)",
                row
            )
    conn.commit()
    cur.close()
    conn.close()


def insert_via_console():
    conn = get_connection()
    cur = conn.cursor()
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    cur.execute(
        f"INSERT INTO {TABLE_NAME} (first_name, last_name, phone) VALUES (%s, %s, %s)",
        (first_name, last_name, phone)
    )
    conn.commit()
    cur.close()
    conn.close()


def update_phonebook(first_name, new_phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        f"UPDATE {TABLE_NAME} SET phone = %s WHERE first_name = %s",
        (new_phone, first_name)
    )
    conn.commit()
    cur.close()
    conn.close()


def query_phonebook(first_name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {TABLE_NAME} WHERE first_name = %s", (first_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()


def delete_from_phonebook(by, value):
    if by not in ['first_name', 'phone']:
        print("Неверное поле для удаления.")
        return
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM {TABLE_NAME} WHERE {by} = %s", (value,))
    conn.commit()
    cur.close()
    conn.close()


def main():
    create_table()
    while True:
        print("\n PhoneBook Menu")
        print("1. Insert from CSV")
        print("2. Insert via console")
        print("3. Update phone number")
        print("4. Query by first name")
        print("5. Delete record")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            file_path = input("Enter CSV file path: ")
            insert_from_csv(file_path)
        elif choice == '2':
            insert_via_console()
        elif choice == '3':
            first_name = input("Enter the first name of the person to update: ")
            new_phone = input("Enter the new phone number: ")
            update_phonebook(first_name, new_phone)
        elif choice == '4':
            first_name = input("Enter the first name to query: ")
            query_phonebook(first_name)
        elif choice == '5':
            by = input("Delete by 'first_name' or 'phone': ")
            value = input("Enter the value: ")
            delete_from_phonebook(by, value)
        elif choice == '6':
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
