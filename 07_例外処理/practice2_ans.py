try:
    # ファイルを読み込む
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    # ファイルが存在しない場合の処理
    print("ファイルが見つかりません。")
except IOError:
    # ファイルの読み込み中にエラーが発生した場合の処理
    print("ファイルの読み込み中にエラーが発生しました。")
