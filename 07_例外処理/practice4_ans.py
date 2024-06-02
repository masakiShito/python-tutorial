# 独自の例外クラスを定義
class NegativeNumberError(Exception):
    pass

try:
    # ユーザーからの入力を受け取る
    number = int(input("正の整数を入力してください: "))
    # 負の数が入力された場合に例外をスローする
    if number < 0:
        raise NegativeNumberError("負の数は入力できません。")
    print(f"入力された数: {number}")
except NegativeNumberError as e:
    # 独自の例外の処理
    print(e)
except ValueError:
    # 無効な入力の処理
    print("無効な入力です。整数を入力してください。")
