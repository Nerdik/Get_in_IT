import tkinter as tk
from tkinter import filedialog
import pandas as pd
import requests
import uuid
import base64
import requests
import json
import tkinter as tk
from tkinter import filedialog
from itertools import chain
from LLM import get_answer_final

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
            #print(df)
            #print(df.columns.tolist())
            #print("---" * 10)   
        global user_data
        user_data = [df.columns.tolist() for df in dfs.values()]
        user_data = list(chain.from_iterable(user_data))
        print(user_data)
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
    df1=pd.DataFrame()
    for sheet_name, df in dfs.items():
        column_names=get_answer_final()
        column_names=eval(column_names)
        print("Ищем следующие имена столбцов в исходном формате:",column_names)
        for column_name in column_names:
            if column_name in get_columns(df):
                # Добавление столбца в новый DataFrame
                print("Есть контакт")
                df1[column_name] = df[column_name]   
    df1.to_excel(file_path_new, index=False)

# Функция для получения списка столбцов из DataFrame
def get_columns(df):
    return df.columns.tolist()
    
def get_user_data():
    return (user_data)


 



