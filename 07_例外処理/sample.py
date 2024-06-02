# -*- coding: utf-8 -*-
# 上記の記述は日本語コメントを含むPythonファイルのエンコーディングを指定しています。

# 独自の例外クラスを定義
class InvalidAgeError(Exception):
    """
    ユーザーが無効な年齢を入力したときにスローされる例外クラス。
    """
    def __init__(self, message):
        super().__init__(message)

def get_valid_age():
    """
    ユーザーに有効な年齢を入力させる関数。
    無効な年齢が入力された場合、InvalidAgeError をスローする。
    """
    try:
        # ユーザーからの入力を受け取る
        age = int(input("年齢を入力してください（0〜120歳）: "))
        # 入力された年齢が無効な場合、InvalidAgeError をスローする
        if age < 0 or age > 120:
            raise InvalidAgeError("無効な年齢です。0〜120歳の範囲で入力してください。")
        print(f"入力された年齢: {age}")
    except InvalidAgeError as e:
        # 独自の例外をキャッチしてエラーメッセージを表示
        print(f"エラー: {e}")
    except ValueError:
        # 無効な入力の処理
        print("無効な入力です。整数を入力してください。")

if __name__ == "__main__":
    # メインの処理
    get_valid_age()
