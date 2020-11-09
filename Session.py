class Session:
    def validate_password(self, password):
        if password == "":
            return False
        elif len(password) >= 8:
            return True
