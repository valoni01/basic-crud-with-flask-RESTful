from model.userModel import UserModel
from flask_restful import Resource, reqparse

class UserList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('firstname',required=True)  
    parser.add_argument('email',required=True)
    parser.add_argument('lastname',required=True)
    parser.add_argument('password',required=True)
    parser.add_argument('_id',required=True)

    def post(self):
        data = UserList.parser.parse_args()
        try:
            user = UserModel.GetUserById(data['_id'])
            if user:
                return {"message":"User Already exist"},201
            else:
                try:
                    newUser = UserModel(**data)
                    newUser.CreatUser()
                    return {"message":"User Created"},201
                except Exception as err:
                    print("Did i fail?")
                    print(err)
        except Exception as err:
            {"message":"errsjjaKAJAKJAKAJASKAJS"},500
    
    def get(self):
        try:
            result = UserModel.GetAllUsers()
            users=[]
            print(result)
            if result:  
                for u in result:
                    row = UserModel(*u)
                    users.append(row.toJson())
                return {"data":users},200
            else:
                return {"data":users,"message":"no records found"}, 404
        except:
            {"message":"server error"},500
    
    def put(self):
        data = UserList.parser.parse_args()
        try:
           user = UserModel.GetUserById(data['_id'])
           if user:
               try:
                   user = UserModel(**data)
                   user.UpdateUser()
                   return {"message":"user updated","data":user.toJson()}, 200
               except:
                   return {"message":"Failed to update user"}, 500
           else:
               return {"message":"user not found"}, 400
        except:
            return {"message":"db error"}, 500


class UserMod(Resource):
    def get(self,_id):
        try:
           user = UserModel.GetUserById(_id)
           if user:
               return {"data":user.toJson()}
           else:
               return {"message":"user not found"}, 404
        except Exception as err:
            print(err)
            return {"message":"server error"},500

    def delete(self,_id):
        try:
            user = UserModel.GetUserById(_id)
            if user:
                UserModel.DeleteUser(_id)
                return {"message":"user deleted"}, 302
            else:
                {"message":"user does not exist"}
        except Exception as err:
            print(err)
            return {"message":"server error"}, 500

                
            
