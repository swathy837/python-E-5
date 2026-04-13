class InvalidLoginError(Exception):
    pass

class AccountLockedError(Exception):
    pass

class LoginSystem:
    def __init__(self, valid_username, valid_password):
        self.username = valid_username
        self.password = valid_password
        self.attempts = 0
        self.is_locked = False

    def login(self):
        while self.attempts < 3:
            if self.is_locked:
                print("Account is already locked.")
                return

            try:
                user_input = input("Enter Username: ")
                pass_input = input("Enter Password: ")
                if user_input == self.username and pass_input == self.password:
                    print("Login successful! Welcome back.")
                    return
                else:
                    self.attempts += 1
                    raise InvalidLoginError("Invalid username or password.")

            except InvalidLoginError as e:
                print("Error: ",e)
                if self.attempts >= 3:
                    self.is_locked = True
                    try:
                        raise AccountLockedError("Too many failed attempts. Your account is now locked.")
                    except AccountLockedError:
                        print("CRITICAL: ",AccountLockedError)
                else:
                    print("Remaining attempts:",3 - self.attempts)

system = LoginSystem("abc", "123")
system.login()
