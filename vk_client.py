
# vk_client.py
import vk_api
import requests
import json

# --- Конфигурация ---
# Токен, который мы получили в Шаге 2
TOKEN=""


#TOKEN = "f9cd0accf9cd0accf9cd0accf2fa8dc9dbff9cdf9cd0acc903a1d0d4d473e1b2f1d5bc0"
vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()

print(vk)
# Адрес вашего локального сервера, где запущен Flask
# Если вы тестируете на том же компьютере, где сервер:
API_URL = "http://127.0.0.1:5000/api/v1/recommend"

def search_communities(query):
    try:
        # Поиск сообществ по ключевой фразе
        response = vk.groups.search(
            q=query,       # Поисковой запрос
            type='group', # Тип: группы или публичные страницы
            count=10,      # Количество результатов (макс. 1000)
            v='5.199'      # Версия API
        )
        
        groups = []
        # Обработка результатов
        if response['items']:
            print(f"Найдено групп: {response['count']}\n")
            for group in response['items']:
                groups.append(group)
                get_last_post(group['id'])
                print(f"{group['name']} (id: {group['id']}) - https://vk.com/{group['screen_name']}")
        else:
            print("Сообщества не найдены.")
            
    except vk_api.exceptions.ApiError as e:
        print(f"Ошибка API: {e}")

def get_last_post(group_id):
    try:
        # group_id для сообществ должен начинаться с минуса
        if not str(group_id).startswith('-'):
            owner_id = -int(group_id)
        else:
            owner_id = group_id

        # Получаем записи со стены
        response = vk.wall.get(
            owner_id=owner_id,
            count=2, # Берем 2, так как первый может быть закрепленным
            v='5.199'
        )

        if response['items']:
            # Проверяем, есть ли закрепленный пост (is_pinned)
            # Если вам нужен именно последний хронологический, 
            # обычно это первый элемент в списке
            post = response['items'][0]
            
            text = post.get('text', '[Нет текста]')
            post_id = post.get('id')
            
            print(f"ID поста: {post_id}")
            print(f"Содержание:\n{text}")
            
            # Если есть вложения (фото и т.д.)
            if 'attachments' in post:
                print(f"\nВложений: {len(post['attachments'])}")
        else:
            print("Стена пуста.")

    except vk_api.exceptions.ApiError as e:
        print(f"Ошибка API: {e}")

# Пример: группа с ID 1 (ВКонтакте)
# Пример использования
search_communities('Python')
