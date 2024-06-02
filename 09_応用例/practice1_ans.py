# file_operations.py

# -*- coding: utf-8 -*-
def file_operations():
    # 'data.txt' というファイルを作成してユーザーからの入力を記録
    with open('data.txt', 'w') as file:
        user_input = input("テキストを入力してください: ")
        file.write(user_input + '\n')

    # ファイルから内容を読み込み表示
    with open('data.txt', 'r') as file:
        content = file.read()
        print('ファイルの内容:')
        print(content)

file_operations()
