import datetime
class User:
    valid = {"username": "admin", "password": "admin"}

    def __init__(self,username="John",password="abcd"):
        self.username= username
        self.password=password

    def check_password(self):
        if self.username==User.valid["username"] and self.password==User.valid['password']:
            print(f'Welcome,{self.username}')
        else:
            print(f'Credentials are invalid!')
    
 
a= User()
a1=User(username="admin",password="admin")
a2=User(username="admin")
a3=User(username="John",password="abcd")
User.check_password(a)
User.check_password(a1)
User.check_password(a2)
User.check_password(a3)
