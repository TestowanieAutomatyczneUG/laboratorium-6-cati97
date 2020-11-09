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