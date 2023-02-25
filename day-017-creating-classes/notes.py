class User:
    def __init__(self, username, user_id):
        self.username = username
        self.id = user_id
        self.followers = 0
        self.following = 0

        print(f"New user {self.username} with id: {self.id} is initialized")

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_one = User('Pacio', 1)
user_two = User('Angela', 2)

user_one.follow(user_two)

print(user_one.following)
print(user_one.followers)

print(user_two.following)
print(user_two.followers)