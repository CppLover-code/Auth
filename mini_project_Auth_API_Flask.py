# Установка pip install flask bcrypt pyjwt
from flask import Flask, request, jsonify
import bcrypt, jwt, datetime

app = Flask(__name__)                     # Создаётся Flask сервер.

SECRET_KEY = "supersecret"                # Секретный ключ для подписи JWT.

users = []                                # Временная база данных. Список пользователей в памяти.

#REGISTER
@app.route("/register", methods=["POST"]) # REGISTER ROUTE, Создаём endpoint, Разрешаем только POST запросы.

def register():                           # Срабатывает при запросе: POST /register

    data = request.get_json()             # Получаем JSON от клиента.
    """
    {
    "username": "mark",
    "password": "1234"
    }
    """

    password = data["password"]           # Получение пароля, Берём пароль из JSON.


    hashed = bcrypt.hashpw(               # Создаёт hash пароля.
        password.encode(),                # bcrypt работает только с bytes.
        bcrypt.gensalt()                  # Создаёт случайную соль. Salt нужен для безопасности.
    )

    user = {                              # СЛОВАРЬ, который хранит данные пользователя
        "username": data["username"],
        "password": hashed
    }
    users.append(user)                     # добавляем пользователя в СПИСОК

    return jsonify({
        "message": "User created"
    })

# LOGIN
@app.route("/login", methods=["POST"])
def login():                            # Функция авторизации.

    data = request.get_json()           # Получаем JSON

    username = data["username"]         # получаем данные пользователя
    password = data["password"]

    for user in users:                 # перебираем пользователей, проверяем данные

        if user["username"] == username:

            if bcrypt.checkpw(          # сравнивает "1234" с hash b"$2b$12$..."
                password.encode(),
                user["password"]
            ):
                
                token = jwt.encode(     # Если пароль правильный Создаём JWT token.
                    {
                        "username": username,
                        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
                    },
                    SECRET_KEY,
                    algorithm="HS256"
                )

                return jsonify({
                    "token": token
                })
    return jsonify({
        "message": "Invalid credentials"
    }), 401

app.run(debug=True) # запуск сервера

"""
Работа программы целиком:
Client
↓
POST /register
↓
Пароль хешируется
↓
Пользователь сохраняется

POST /login
↓
Проверка пароля
↓
Создание JWT
↓
Возврат токена
"""

