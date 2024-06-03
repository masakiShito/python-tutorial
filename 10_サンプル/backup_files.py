import os
import shutil
import datetime

def backup_files(source_dir, backup_dir):
    """
    指定したディレクトリ内のファイルをバックアップする。

    Parameters:
    - source_dir: バックアップ元のディレクトリ
    - backup_dir: バックアップ先のディレクトリ
    """
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    backup_subdir = os.path.join(backup_dir, f'backup_{timestamp}')

    shutil.copytree(source_dir, backup_subdir)
    print(f"ファイルを {backup_subdir} にバックアップしました。")

if __name__ == "__main__":
    source_directory = "path/to/source_dir"  # バックアップ元のディレクトリ
    backup_directory = "path/to/backup_dir"  # バックアップ先のディレクトリ

    backup_files(source_directory, backup_directory)
