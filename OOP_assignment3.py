
# username = input("What is your username? ")
# password = input(f"Type the password for username {username}: ")

# def get_user(username,password):
   
#     for user in users:
#         if username == user['name'] and password == user['password']:
#             return user
        
#     print(f'An error occured. You are not authorized.')
#     return None      
      
        
# user = get_user(username,password)
class Users():
        users = [
        {
            "name": "Holly",
            "password": "hunter"
        },
        {
            "name": "Peter",
            "password": "pan"
        },
        {
            "name": "Janis",
            "password": "joplin"
        }
    ]
        def __init__(self,username,password):
            #instance/object method
            self.username = username
            self.password = password

        def get_user(self):
    
            for user in Users.users:
                if self.username == user['name'] and self.password == user['password']:
                    return f"You are allowed"
                
            return f'An error occured. You are not authorized.'
                  

user1=Users("Holly","hunter")
user2=Users("Peter","pedro")
user3=Users("Janis","joplin")
print(user1.get_user())
print(user2.get_user())
print(user3.get_user())