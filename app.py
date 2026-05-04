# app.py
from flask import Flask, jsonify, send_from_directory, request
import random

app = Flask(__name__, static_folder='frontend')

# Роут для индексного файла (главная страница)
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Пример базы рекомендаций (можно заменить на ML-модель или данные из VK)
RECOMMENDATIONS = {
    'технологии': [
        {'title': 'VK Mini Apps: новые возможности', 'url': 'https://vk.com/dev/mini_apps', 'desc': 'Обзор новых функций платформы.'},
        {'title': 'Python 4.0: что нового?', 'url': '#', 'desc': 'Главные изменения в языке.'},
    ],
    'спорт': [
        {'title': 'Чемпионат по киберспорту', 'url': '#', 'desc': 'Лучшие команды сразятся в финале.'},
    ],
    'культура': [
        {'title': 'Выставка современного искусства', 'url': '#', 'desc': 'Открытие в Москве.'},
    ],
}

@app.route('/api/v1/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('user_id')
    # В реальном приложении здесь будет логика ML или выбор по интересам пользователя
    # Для примера — возвращаем случайные рекомендации
    topic = random.choice(list(RECOMMENDATIONS.keys()))
    result = RECOMMENDATIONS[topic]
    return jsonify({'user_id': user_id, 'recommendations': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
