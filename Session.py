class Session:
    def validate_password(self, password):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
        digits = "0123456789"
        special_symbols = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}
        if len(password) >= 8:
            for letter in password:
                if letter in alphabet:
                    for digit in password:
                        if digit in digits:
                            for symbol in password:
                                if symbol in special_symbols:
                                    return True
                                else:
                                    continue
                            return False
                        else:
                            continue
                    return False
                else:
                    continue
            return False
        else:
            return False
