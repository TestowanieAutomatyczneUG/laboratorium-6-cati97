class Session:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def validate_password(self, password):
        if len(password) >= 8:
            return True
        else:
            return False
