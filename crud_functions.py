import sqlite3


def initiate_db():
    db_products = sqlite3.connect('db_products.db')
    cursor_db_products = db_products.cursor()

    cursor_db_products.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL,
            photo TEXT
            )
        '''
        )

    for i in range(1, 5):
        db_products.execute('''INSERT INTO Products (title, description, price, photo) VALUES(?, ?, ?, ?)''',
            (f'Product {i}', f'Описание {i}', i * 100, f'photo/photo{i}.jpeg'))

    db_products.commit()
    db_products.close()

def get_all_products():
    db_products = sqlite3.connect('db_products.db')
    cursor_db_products = db_products.cursor()

    result = cursor_db_products.execute('''SELECT * FROM Products''').fetchall()
    db_products.close()
    return result


if __name__ == '__main__':
    initiate_db()
    print(get_all_products())