import tkinter as tk
from tkinter import filedialog
import pandas as pd

# Функция загрузки файла
def get_file():
    root = tk.Tk()
    root.withdraw() # Убираем главное окно, оставляя только окно диалога
    # Открываем диалог выбора файла
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    print("Путь к файлу",file_path) 
    if file_path:
        # Чтение данных из выбранного файла Excel, получаем массив pandas     
        global dfs #словарь данных, где ключи -названия листов, а значения соответствующие массивы данных для одного листа
        global excel_file_init #исходный файл экселя
        #получение исходного файла экселя
        excel_file_init=pd.ExcelFile(file_path)
        # Получение списка имен всех листов в файле
        global all_sheet_names
        all_sheet_names = excel_file_init.sheet_names
        dfs={}
        for sheet_name in all_sheet_names:
            # Чтение данных из конкретного листа Excel
            dfs[sheet_name] = pd.read_excel(file_path, sheet_name=sheet_name)
         # Вывод информации о каждом DataFrame
        for sheet_name, df in dfs.items():
            print(f"Sheet Name: {sheet_name}")
            print(df)
            print("---" * 10)   
    else:
        print("Файл не выбран.")
    return dfs, file_path

#функция, которая создает путь для нового файла excel,
def add_new_to_filepath():
    # Разделяем путь на элементы
    path_elements = file_path.split('/')   
    # Находим последний элемент (имя файла)
    last_element = path_elements[-1]
    # Разделяем имя файла и расширение
    filename, extension = last_element.rsplit('.', maxsplit=1)
    # Формируем новое имя файла с добавлением "_new"
    global file_path_new
    file_path_new = f"{filename}_new"
    # Формируем новый путь файла
    file_path_new = '/'.join(path_elements[:-1]) + '/' + file_path_new + '.' + extension
    print(file_path_new)
    return file_path_new

#функция выгрузки файла
def output_file():    
    add_new_to_filepath()
    list(dfs.values())[0].to_excel(file_path_new, index=False)




