# JWT (JSON Web Token)
"""
JWT — специальный токен для авторизации.

После логина сервер выдает токен: eyJhbGciOiJIUzI1NiIsInR5cCI...
Клиент отправляет его в запросах.
"""
# Установка JWT библиотеки
# pip install pyjwt

# Создание JWT токена
import jwt
import datetime

SECRET_KEY = "supersecret"

payload = {
    "user_id": 1,
    "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=1)
}
token = jwt.encode(
    payload,
    SECRET_KEY,
    algorithm="HS256"
)

print(f"Encoded {token}")

# Расшифровка токена
data = jwt.decode(
    token,
    SECRET_KEY,
    algorithms=["HS256"]
)

print(f"Decoded {data}")