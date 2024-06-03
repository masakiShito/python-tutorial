import csv

def write_csv(data, filename):
    """
    データをCSVファイルに書き込む。

    Parameters:
    - data: 書き込むデータ（リスト形式）
    - filename: 書き込み先のファイル名
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
        print(f"{filename} にデータを書き込みました。")

def read_csv(filename):
    """
    CSVファイルからデータを読み込む。

    Parameters:
    - filename: 読み込むファイル名
    """
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        print(f"{filename} からデータを読み込みました。")
        return data

if __name__ == "__main__":
    data_to_write = [
        ["name", "age", "city"],
        ["John", 30, "New York"],
        ["Anna", 22, "London"],
        ["Mike", 32, "San Francisco"]
    ]
    filename = 'data.csv'

    write_csv(data_to_write, filename)
    data = read_csv(filename)
    print(data)
