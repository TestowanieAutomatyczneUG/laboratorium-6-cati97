class Session:
    def validate_password(self, passwd):
        """
        >>> s = Session()
        >>> s.validate_password("")
        False
        >>> s.validate_password("mojehaslohaslo")
        False
        >>> s.validate_password("moje")
        False
        >>> s.validate_password("mojeHaslo2020")
        False
        >>> s.validate_password("mojemalehaslo")
        False
        >>> s.validate_password("haslo3Wielkie")
        False
        >>> s.validate_password("MojeWielkie20!")
        True
        >>> s.validate_password("Duze?has201hm")
        True
        >>> s.validate_password("2134Haslomm*m")
        True
        >>> s.validate_password("2134aslomm*m")
        False
        >>> s.validate_password("2134abcdE?")
        False
        >>> s.validate_password("2134EBASDFGG?")
        True
        """
        special_symbols = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}

        if type(passwd) == str:
            if not any(char == " " for char in passwd):
                if len(passwd) < 10:  # 8 letters (small or capital), 1 symbol, 1 digit
                    return False

                elif not any(char.isdigit() for char in passwd):
                    return False

                elif not any(char.isupper() for char in passwd):
                    return False

                elif sum(1 for c in passwd if c.islower() or c.isupper()) < 7:
                    return False

                elif not any(char in special_symbols for char in passwd):
                    return False

                else:
                    return True
            else:
                raise ValueError("Password cannot contain whitespaces!")
        else:
            raise ValueError("Password must of type string")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
