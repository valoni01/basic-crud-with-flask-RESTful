from flask import Flask
from flask_restful import Api
from resource.UserResource import UserList,UserMod

app = Flask(__name__)
api = Api(app)

api.add_resource(UserList,'/user','/users')
api.add_resource(UserMod,'/user/<string:_id>')

if __name__ == "__main__":
    app.run(debug=True,port=5000)
