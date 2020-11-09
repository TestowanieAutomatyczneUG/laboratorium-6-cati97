class Hamming:
    def distance(self, first, second):
        """
        >>> ham = Hamming()
        >>> ham.distance("", "")
        0
        >>> ham.distance("A", "A")
        0
        >>> ham.distance("G", "T")
        1
        >>> ham.distance("GGACTGAAATCTG", "GGACTGAAATCTG")
        0
        >>> ham.distance("GGACGGATTCTG", "AGGACGGATTCT")
        9
        >>> ham.distance("AATG", "AAA")
        Traceback (most recent call last):
          File "C:\\Users\\Katarzyna\\AppData\\Local\\Programs\\Python\\Python36\\lib\\doctest.py", line 1330, in __run
            compileflags, 1), test.globs)
          File "<doctest __main__.Hamming.distance[6]>", line 1, in <module>
            ham.distance("AATG", "AAA")
          File "C:/Users/Katarzyna/Desktop/3 semestr/Testowanie Automatyczne/lab6/laboratorium-6-cati97/zad1.py", line 27, in distance
            raise ValueError("Strands must have the same length")
        ValueError: Strands must have the same length
        """
        if len(first) == len(second):
            count_diff = 0
            for i in range(len(first)):
                if first[i] != second[i]:
                    count_diff += 1
                else:
                    continue
            return count_diff
        else:
            raise ValueError("Strands must have the same length")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # doctest.testmod(extraglobs={'c': Calculate()})

#Odpalenie: python3 DocTestExample.py -v verbose - see all that happens