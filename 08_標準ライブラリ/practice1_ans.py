# -*- coding: utf-8 -*-
import os

def os_module_practice():
    # 現在のディレクトリを取得
    current_dir = os.getcwd()
    print(f"現在のディレクトリ: {current_dir}")

    # 新しいディレクトリ 'test_dir' を作成
    os.mkdir('test_dir')
    print("'test_dir' を作成しました")

    # 作成したディレクトリに移動
    os.chdir('test_dir')
    print(f"'test_dir' に移動しました。現在のディレクトリ: {os.getcwd()}")

    # 元のディレクトリに戻る
    os.chdir(current_dir)
    print(f"元のディレクトリに戻りました。現在のディレクトリ: {os.getcwd()}")

    # 作成したディレクトリを削除
    os.rmdir('test_dir')
    print("'test_dir' を削除しました")

os_module_practice()
