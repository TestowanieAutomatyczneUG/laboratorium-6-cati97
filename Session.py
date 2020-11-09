class Session:
    def validate_password(self, password):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
        if len(password) >= 8:
            for symbol in password:
                if symbol in alphabet:
                    return True
                else:
                    continue
            return False
        else:
            return False
