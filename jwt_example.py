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

SECRET_KEY = "supersecret" # Это ключ, которым подписывается токен. 
# С его помощью сервер: создаёт токен, потом проверяет, что токен не подделан
# Если злоумышленник узнает этот ключ — он сможет создавать свои токены.
# Поэтому в реальных проектах: ключ длинный, сложный, хранится в .env

payload = {                     
    "user_id": 1,
    "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=1) 
}
"""
Payload — данные внутри токена
JWT состоит из: Header, Payload, Signature
Payload — это полезные данные.
"user_id": 1 - означает, что токен принадлежит пользователю с id = 1
"exp" — expiration time - Тут создаётся время окончания действия токена.

datetime.datetime.utcnow() - Получаем текущее время UTC.
UTC используется потому что: это мировой стандарт, нет проблем с часовыми поясами

datetime.timedelta(hours=1) - Создаёт промежуток времени 1 час

Можно так:

datetime.timedelta(days=7)
datetime.timedelta(minutes=30)
Сложение
datetime.datetime.utcnow() + datetime.timedelta(hours=1)

означает:

текущее время + 1 час

То есть токен станет недействительным через час.
"""
token = jwt.encode(    # jwt.encode() кодирует данные в JWT.
    payload,
    SECRET_KEY,
    algorithm="HS256"  # Алгоритм шифрования/подписи. HS256: самый популярный, использует секретный ключ
)

print(f"ENCODED {token}")

# Расшифровка токена
data = jwt.decode(
    token,
    SECRET_KEY,
    algorithms=["HS256"]
)

print(f"DECODED {data}")

# Что хранится внутри JWT


