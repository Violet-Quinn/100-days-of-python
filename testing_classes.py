class User:
    def __init__(self,user_id,username):
        self.id=user_id
        self.name=username


user1=User("001","adam")

print(user1.name)