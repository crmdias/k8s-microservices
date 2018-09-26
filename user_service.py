from flask import Flask, request
import pymongo
import jwt
app = Flask(__name__)

uri = "mongodb://workshop:1a2b3c4d@ds047950.mlab.com:47950/todo"

client = pymongo.MongoClient(uri)

db = client.get_default_database()

@app.route("/user/auth")
def user_auth():
    username = request.headers.get('username')
    password = request.headers.get('password')
    if not username:
        return "{\"message\": \"Bad request: username missing\"}", 400
    if not password:
        return "{\"message\": \"Bad request: password missing\"}", 400

    try:
        user = db['workshop_users'].find({'username': username, 'password': password})[0]
    except Exception as e:
        print(e)
        return "{\"message\": \"Unable to authenticate with the given user\"}", 403

    return jwt.encode({'user_id': user["id"]}, '31AB8F2718655495D5347A325FA9A', algorithm='HS256'), 200
    
if __name__ == "__main__":
    app.run()
