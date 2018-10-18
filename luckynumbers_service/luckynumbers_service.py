from flask import Flask, request
import jwt
import random

app = Flask(__name__)


def generate_random_numbers():
    numbers = sorted(random.sample(range(1, 61), 6))
    return '-'.join([str(i) for i in numbers])


@app.route("/numbers")
def get_music():
    auth_token = request.headers.get('authorization')
    if not auth_token:
        return "{\"message\": \"Bad request: auth_token missing\"}", 400

    try:
        user_id = jwt.decode(
            auth_token, '31AB8F2718655495D5347A325FA9A', algorithm='HS256')['user_id']
    except Exception as e:
        print(e)
        return "{\"message\": \"Unable to authenticate with the given user\"}", 403

    return '{\"numbers\": \"' + generate_random_numbers() + '\" }'


if __name__ == "__main__":
    app.run(host='localhost', port=9876)
