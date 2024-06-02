try:
    # ユーザーから1つ目の整数を入力させる
    num1 = int(input("1つ目の整数を入力してください: "))
    # ユーザーから2つ目の整数を入力させる
    num2 = int(input("2つ目の整数を入力してください: "))
    # 2つの整数を除算する
    result = num1 / num2
    print(f"結果は: {result}")
except ZeroDivisionError:
    # ゼロ除算エラーの処理
    print("ゼロで除算することはできません。")
except ValueError:
    # 無効な入力の処理
    print("無効な入力です。整数を入力してください。")
finally:
    # 最後に必ず実行される処理
    print("プログラムが終了しました。")
