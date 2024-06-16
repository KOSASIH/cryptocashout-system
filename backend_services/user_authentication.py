import hashlib

class UserAuthentication:
    def __init__(self):
        self.users = {"user1": "password1", "user2": "password2"}

    def authenticate(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if username in self.users and self.users[username] == hashed_password:
            return True
        return False
