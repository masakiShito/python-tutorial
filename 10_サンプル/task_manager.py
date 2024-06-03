import sqlite3

# データベースの初期化
def initialize_db():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# タスクの追加
def add_task(title, description):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)
    ''', (title, description, '未完了'))
    conn.commit()
    conn.close()
    print(f"タスク '{title}' を追加しました。")

# タスクの表示
def list_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()

    if tasks:
        for task in tasks:
            print(f"ID: {task[0]}, タイトル: {task[1]}, 説明: {task[2]}, 状態: {task[3]}")
    else:
        print("タスクはありません。")

# タスクの削除
def delete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    print(f"タスク ID '{task_id}' を削除しました。")

# タスクの完了状態の変更
def complete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET status = ? WHERE id = ?', ('完了', task_id))
    conn.commit()
    conn.close()
    print(f"タスク ID '{task_id}' を完了状態に変更しました。")

# メイン関数
def main():
    initialize_db()

    while True:
        print("\nタスク管理システム")
        print("1. タスクを追加")
        print("2. タスクを表示")
        print("3. タスクを削除")
        print("4. タスクを完了にする")
        print("5. 終了")

        choice = input("選択してください (1-5): ")

        if choice == '1':
            title = input("タスクのタイトル: ")
            description = input("タスクの説明: ")
            add_task(title, description)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            task_id = int(input("削除するタスクのID: "))
            delete_task(task_id)
        elif choice == '4':
            task_id = int(input("完了にするタスクのID: "))
            complete_task(task_id)
        elif choice == '5':
            print("終了します。")
            break
        else:
            print("無効な選択です。もう一度お試しください。")

if __name__ == "__main__":
    main()
