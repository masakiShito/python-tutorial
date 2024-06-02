try:
    # ユーザーからの入力を受け取る
    user_input = input("整数を入力してください: ")
    # 入力された値を整数に変換する
    number = int(user_input)
    print(f"入力された整数は: {number}")
except ValueError:
    # 整数に変換できない場合にエラーメッセージを表示する
    print("無効な入力です。整数を入力してください。")
