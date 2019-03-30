import sqlite3 

class UserModel:
    def __init__(self,_id,firstname,lastname,email,password):
        self.id = _id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    def toJson(self):
        return {
            "id":self.id,
            "firstname":self.firstname,
            "lastname":self.lastname,
            "email":self.email,
        }

    def CreatUser(self):
        connect = sqlite3.connect('data.db')
        cursor = connect.cursor()
        query = "insert into users values(?,?,?,?,?)"
        cursor.execute(query,(self.id,self.firstname,self.lastname,self.email,self.password))
        connect.commit()
        connect.close()

    @classmethod
    def GetUserById(cls,_id):
        connect = sqlite3.connect('data.db')
        cursor = connect.cursor()
        query = "select * from users where id = ?"
        result = cursor.execute(query,(_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None 
        connect.close()
        return user

    def UpdateUser(self):
        connect = sqlite3.connect('data.db')
        cursor = connect.cursor()
        query = "update users set firstname = ?, lastname = ? where id = ?"
        cursor.execute(query,(self.firstname,self.lastname,self.id))
        connect.commit()
        connect.close()
    
    @classmethod
    def GetAllUsers(cls):
        connect = sqlite3.connect('data.db')
        cursor = connect.cursor()
        query = "select * from users"
        result = cursor.execute(query)
        if result:
            return result
        else:
            return False
        connect.close()
    
    @classmethod
    def DeleteUser(cls,_id):
        connect = sqlite3.connect('data.db')
        cursor = connect.cursor()
        query = "delete from users where id = ?"
        cursor.execute(query,(_id,))
        connect.commit()
        connect.close()


        
