import os
import sys
import subprocess

project_root = os.path.abspath('../')

paths = {
    "pz_6": os.path.join(project_root, 'ПЗ№6'),
    "pz_7": os.path.join(project_root, 'ПЗ№7', 'pz_7_1.py'),
    "pz_11": os.path.join(project_root, 'ПЗ№11'),
    "test": os.path.join(project_root, 'test'),
    "test1": os.path.join(project_root, 'test', 'test1'),
    "test_file": os.path.join(project_root, 'test', 'test1', 'test.txt'),
    "reports": os.path.join(project_root, 'reports'),
    "report_pdf": 'PZ_7.pdf'
}


def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])


def change_directory(path):
    if os.path.exists(path):
        os.chdir(path)
        return True
    else:
        print(f"Каталог {path} не найден")
        return False


def copy_file(source, destination):
    if os.path.exists(source):
        with open(source, 'rb') as f_src, open(destination, 'wb') as f_dst:
            f_dst.write(f_src.read())
    else:
        print(f"Файл {source} не найден")


def list_files_in_directory(path):
    if os.path.exists(path):
        os.chdir(path)
        return [f for f in os.listdir() if os.path.isfile(f)]
    else:
        print(f"Каталог {path} не найден")
        return []


def create_directory(path):
    os.makedirs(path, exist_ok=True)


def print_file_sizes(directory):
    if os.path.exists(directory):
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        for file in files:
            file_path = os.path.join(directory, file)
            print(f"Размер файла {file}: {os.path.getsize(file_path)} байт")
    else:
        print(f"Каталог {directory} не найден")


os.chdir(project_root)

files_in_pz11 = list_files_in_directory(paths['pz_11'])

print("Файлы в каталоге PZ_11:", files_in_pz11)

create_directory(paths['test1'])

files_to_copy = ['pz-6-1.py', 'pz-6-2.py']
for file in files_to_copy:
    src = os.path.join(paths['pz_6'], file)
    dst = os.path.join(paths['test'], file)
    copy_file(src, dst)

copy_file(paths['pz_7'], paths['test_file'])

print_file_sizes(paths['test'])

if files_in_pz11:
    shortest_filename = min(files_in_pz11, key=len)
    print("Файл с самым коротким именем:", os.path.basename(shortest_filename))


if change_directory(paths['reports']) and os.path.exists(paths['report_pdf']):
    open_file(paths['report_pdf'])
else:
    print(f"PDF файл {paths['report_pdf']} не найден")


if os.path.exists(paths['test_file']):
    os.remove(paths['test_file'])
    print(f"Файл {paths['test_file']} успешно удален")
else:
    print(f"Файл {paths['test_file']} не найден для удаления")
