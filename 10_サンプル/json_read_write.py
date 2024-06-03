import json

def write_json(data, filename):
    """
    データをJSONファイルに書き込む。

    Parameters:
    - data: 書き込むデータ（辞書形式）
    - filename: 書き込み先のファイル名
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
        print(f"{filename} にデータを書き込みました。")

def read_json(filename):
    """
    JSONファイルからデータを読み込む。

    Parameters:
    - filename: 読み込むファイル名
    """
    with open(filename, 'r') as file:
        data = json.load(file)
        print(f"{filename} からデータを読み込みました。")
        return data

if __name__ == "__main__":
    data_to_write = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    filename = 'data.json'

    write_json(data_to_write, filename)
    data = read_json(filename)
    print(data)
