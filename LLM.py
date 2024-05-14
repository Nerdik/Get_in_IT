import requests
import uuid
import base64
import requests
import json
import tkinter as tk
from tkinter import filedialog
import pandas as pd

def Get_Answer_LLM(user_request01,user_data01):
    client_id = '42be7677-cdfd-42bf-a857-c7648d87d36a'
    secret = '05687c0c-012c-43c8-b199-8d8dbcb7dbdc'
    auth = 'NDJiZTc2NzctY2RmZC00MmJmLWE4NTctYzc2NDhkODdkMzZhOjA1Njg3YzBjLTAxMmMtNDNjOC1iMTk5LThkOGRiY2I3ZGJkYw=='
    credentials = f"{client_id}:{secret}"
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

    encoded_credentials == auth

    def get_token(auth_token, scope='GIGACHAT_API_PERS'):
        """
        Выполняет POST-запрос к эндпоинту, который выдает токен.

        Параметры:
        - auth_token (str): токен авторизации, необходимый для запроса.
        - область (str): область действия запроса API. По умолчанию — «GIGACHAT_API_PERS».

        Возвращает:
        - ответ API, где токен и срок его "годности".
        """
        # Создадим идентификатор UUID (36 знаков)
        rq_uid = str(uuid.uuid4())

        # API URL
        url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

        # Заголовки
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'RqUID': rq_uid,
            'Authorization': f'Basic {auth_token}'
        }

        # Тело запроса
        payload = {
            'scope': scope
        }

        try:
            # Делаем POST запрос с отключенной SSL верификацией
            # (можно скачать сертификаты Минцифры, тогда отключать проверку не надо)
            response = requests.post(url, headers=headers, data=payload, verify=False)
            return response
        except requests.RequestException as e:
            print(f"Ошибка: {str(e)}")
            return -1

    response = get_token(auth)
    if response != 1:
        print(response.text)
    giga_token = response.json()['access_token']
    
    

    url = "https://gigachat.devices.sberbank.ru/api/v1/models"

    payload={}
    headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {giga_token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)

    #print(response.text)  

    def get_chat_completion(auth_token, user_message):
        """
        Отправляет POST-запрос к API чата для получения ответа от модели GigaChat.

        Параметры:
        - auth_token (str): Токен для авторизации в API.
        - user_message (str): Сообщение от пользователя, для которого нужно получить ответ.

        Возвращает:
        - str: Ответ от API в виде текстовой строки.
        """
        # URL API, к которому мы обращаемся
        url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

        # Подготовка данных запроса в формате JSON
        payload = json.dumps({
            "model": "GigaChat",  # Используемая модель
            "messages": [
                {
                    "role": "user",  # Роль отправителя (пользователь)
                    "content": user_message  # Содержание сообщения
                }
            ],
            "temperature": 1,  # Температура генерации
            "top_p": 0.1,  # Параметр top_p для контроля разнообразия ответов
            "n": 1,  # Количество возвращаемых ответов
            "stream": False,  # Потоковая ли передача ответов
            "max_tokens": 512,  # Максимальное количество токенов в ответе
            "repetition_penalty": 1,  # Штраф за повторения
            "update_interval": 0  # Интервал обновления (для потоковой передачи)
        })

        # Заголовки запроса
        headers = {
            'Content-Type': 'application/json',  # Тип содержимого - JSON
            'Accept': 'application/json',  # Принимаем ответ в формате JSON
            'Authorization': f'Bearer {auth_token}'  # Токен авторизации
        }

        # Выполнение POST-запроса и возвращение ответа
        try:
            response = requests.request("POST", url, headers=headers, data=payload, verify=False)
            return response
        except requests.RequestException as e:
            # Обработка исключения в случае ошибки запроса
            print(f"Произошла ошибка: {str(e)}")
            return -1    
    answer = get_chat_completion(giga_token, f'У меня есть столбцы с наименованиями:{user_data01} Сейчас будет запрос от пользователя, в котором он попросит составить таблицу из каких то этих столбцов, при этом наименования не всегда совпадают, тебе нужно будет найти ближайшее по значению, в качестве результата верни из исходных только названия столбцов в [] через знак , .Запрос пользователя: {user_request01}')
    answer.json()
    print("ОТВЕТ ОТ ГИГАЧАТА: ",answer.json()['choices'][0]['message']['content'],"------ОТВЕТ ЗАКОНЧЕН")
    global answer_final
    answer_final=answer.json()['choices'][0]['message']['content']
    return answer_final

def get_answer_final():
    return answer_final     
    
 