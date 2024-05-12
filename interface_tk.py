from tkinter import *
from output import get_file,output_file

root = Tk()

root['bg'] ='#0080ff'
root.title('Uranium table unifier')
root.wm_attributes('-alpha', 1)
root.geometry('800x400')

# Неизменяемость размеров окна
root.resizable(width=False, height=False)

# Окно блока для загрузки файла
frame_file = Frame(root, bg='#0080ff')
frame_file.place(relx=0, rely=0, relwidth=1, relheight=0.2)

# Кнопка загрузки файла
btn_file = Button(frame_file, text='Загрузить файл', command=get_file)
btn_file.pack(anchor=N, pady=10)

# Кнопка выгрузки файла
btn_file2 = Button(frame_file, text='Выгрузить файл', command=output_file)
btn_file2.pack(anchor=S, pady=0)

# Окно для блока выбора команд
frame_commands = Frame(root, bg='#0080ff', borderwidth=2, relief="solid")
frame_commands.place(relx=0.02, rely=0.2, relwidth=0.47, relheight=0.65)

# Наиемнование блока
label_commands = Label(frame_commands, text='Выберите команды', bg='#0080ff')
label_commands.pack(anchor=N)

# Чекбокс 
checkbox = ["Объединить данные",
            "Найти повторяющиеся данные",
            "Составить словарь",
            "Редактировать словарь"]

for i in range(len(checkbox)):
    cb_join = Checkbutton(frame_commands, text=checkbox[i], variable=vars, width=40, anchor=W, bg='#00c0ff')
    cb_join.pack(anchor=N, pady=10)


# Окно для блока пользовательской таблицы
frame_table = Frame(root, bg='#0080ff', borderwidth=2, relief="solid")
frame_table.place(relx=0.51, rely=0.2, relwidth=0.47, relheight=0.65)

# Наиемнование блока
label_table = Label(frame_table, text='Пользовательская таблица', bg='#0080ff')
label_table.grid(row=0, column=0, padx=5, pady=0, sticky=E)

# Текстовые поля Наименование столбца и кнопки записи
num_fields = 4
for i in range(num_fields):
    nameField1 = Entry(frame_table, bg='#00c0ff', width=40)
    nameField1.grid(row=i+1, column=0, padx=5, pady=10)
    nameField1.insert(0, 'Введите наименование столбца')
    btn_save1 = Button(frame_table, text=' Записать ', command=get_file)
    btn_save1.grid(row=i+1, column=1, padx=5, pady=10)


root.mainloop()