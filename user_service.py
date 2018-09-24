from flask import Flask
import jwt
app = Flask(__name__)

uri = "mongodb://workshop:1a2b3c4d@ds047950.mlab.com:47950/todo"

client = pymongo.MongoClient(uri)

db = client.get_default_database()

@app.route("/user/auth")
def user_auth():
    #se user existe com essas credenciais
    return jwt.encode({'user_id': user.id}, '31AB8F2718655495D5347A325FA9A', algorithm='HS256')
    #se nao
    #403 na tua cara
