class Session:
    def validate_password(self, password):
        if password == "":
            return False