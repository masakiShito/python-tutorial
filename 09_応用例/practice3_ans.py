# inventory_management.py

# -*- coding: utf-8 -*-
import sqlite3

def database_operations():
    # データベースに接続（存在しない場合は作成されます）
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    # テーブルの作成
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')

    # 商品の追加
    cursor.execute('''
        INSERT INTO inventory (product_name, quantity) VALUES ('Apple', 50)
    ''')
    cursor.execute('''
        INSERT INTO inventory (product_name, quantity) VALUES ('Banana', 30)
    ''')
    conn.commit()

    # 商品の一覧表示
    cursor.execute('SELECT * FROM inventory')
    products = cursor.fetchall()
    print('在庫一覧:')
    for product in products:
        print(f'商品名: {product[1]}, 数量: {product[2]}')

    # データベース接続を終了
    conn.close()

database_operations()
