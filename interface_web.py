import streamlit as st


st.set_page_config(
    page_title='Uranium table unifier',
    layout='wide',
    menu_items={
        'About': "# Uranium table unifier\nПриложение создано командой Uranium в рамках проекта 'Зайтив АйТи'"
    }
)

# Размещение лейблов
col1, col2 = st.columns(2)

with col1:
    st.image('images/GS.jpg', width=200)

with col2:
    st.image('images/VSE.jpg', width=200)


uploaded_files = st.file_uploader("Выберите файл формата .xls, .xlsx", accept_multiple_files=True, type=["xls", "xlsx"])
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("Имя файла:", uploaded_file.name)
    st.write(bytes_data)

# Колонки для форматирования страницы
col1, col2 = st.columns([1, 1])

# Левая колонка для размещения чекбоксов команд
with col1:
    selected = st.checkbox
    st.header("Выберите команды")
    # Список чекбоксов
    cb_list = ["Объединить данные",
                "Найти повторяющиеся данные",
                "Составить словарь",
                "Редактировать словарь"]
    # Чекбоксы
    for i in range(len(cb_list)):
        selected = st.checkbox(cb_list[i])

with col2:
    st.header("Пользовательская таблица")
    # Количество столбцов в итоговой таблице
    num_col = 4
    # Текстовые поля Наименование столбца
    for i in range(num_col):
        st.text_input(f'Введите наименование столбца {i+1}')
