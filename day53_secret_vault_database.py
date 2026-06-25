import sqlite3
conn = sqlite3.connect("vault.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS vault_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    secret_name TEXT NOT NULL,
    secret_code TEXT NOT NULL
)
""")

def add_record(secret_name, secret_code):
    cursor.execute(
        "INSERT INTO vault_records (secret_name, secret_code) VALUES (?, ?)",
        (secret_name, secret_code)
    )
    conn.commit()


def view_records():
    cursor.execute("SELECT * FROM vault_records")
    records = cursor.fetchall()

    print("\nVault Records:")
    for record in records:
        print(record)


def update_record(record_id, new_code):
    cursor.execute(
        "UPDATE vault_records SET secret_code=? WHERE id=?",
        (new_code, record_id)
    )
    conn.commit()

def delete_record(record_id):
    cursor.execute(
        "DELETE FROM vault_records WHERE id=?",
        (record_id,)
    )
    conn.commit()

def search_record(secret_name):
    cursor.execute(
        "SELECT * FROM vault_records WHERE secret_name=?",
        (secret_name,)
    )

    result = cursor.fetchall()

    print("\nSearch Result:")
    for row in result:
        print(row)

add_record("Project X", "A123")
add_record("Mission Alpha", "B456")

view_records()

search_record("Project X")

update_record(1, "X999")

print("\nAfter Update:")
view_records()

delete_record(2)

print("\nAfter Delete:")
view_records()

conn.close()