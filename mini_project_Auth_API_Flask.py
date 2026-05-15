# Установка pip install flask bcrypt pyjwt
from flask import Flask, request, jsonify
import bcrypt, jwt, datetime

app = Flask(__name__)

SECRET_KEY = "supersecret"

users = []

#REGISTER
@app.route("/register", method=["POST"])

def register():

    data = request.get_json()

    password = data["password"]

    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    user = {
        "username": data["username"],
        "password": hashed
    }
    user.append(user)

    return jsonify({
        "message": "User created"
    })

# LOGIN
@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data["username"]
    password = data["password"]

    for user in users:

        if user["username"] == username:

            if bcrypt.checkpw(
                password.encode(),
                user["password"]
            ):
                
                token = jwt.encode(
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

app.run(debug=True)
