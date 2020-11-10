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
        >>> s.validate_password("Pogodaladna 2020$")
        Traceback (most recent call last):
          File "C:\\Users\\Katarzyna\\AppData\\Local\\Programs\\Python\\Python36\\lib\\doctest.py", line 1330, in __run
            compileflags, 1), test.globs)
          File "<doctest __main__.Session.validate_password[13]>", line 1, in <module>
            s.validate_password("Pogodaladna 2020$")
          File "C:/Users/Katarzyna/Desktop/3 semestr/Testowanie Automatyczne/lab6/laboratorium-6-cati97/Session.py", line 53, in validate_password
            raise ValueError("Password cannot contain whitespaces!")
        ValueError: Password cannot contain whitespaces!
        >>> s.validate_password(15)
        Traceback (most recent call last):
          File "C:\\Users\\Katarzyna\\AppData\\Local\\Programs\\Python\\Python36\\lib\\doctest.py", line 1330, in __run
            compileflags, 1), test.globs)
          File "<doctest __main__.Session.validate_password[13]>", line 1, in <module>
            s.validate_password(15)
          File "C:/Users/Katarzyna/Desktop/3 semestr/Testowanie Automatyczne/lab6/laboratorium-6-cati97/Session.py", line 53, in validate_password
            raise ValueError("Password must of type string")
        ValueError: Password must of type string
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
