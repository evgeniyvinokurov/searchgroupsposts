from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Отдаем главную страницу
    return render_template('index.html')    

if __name__ == '__main__':
    # Для локальных тестов в ВК нужен HTTPS. 
    # adhoc генерирует временный сертификат.
    app.run(host='0.0.0.0')
