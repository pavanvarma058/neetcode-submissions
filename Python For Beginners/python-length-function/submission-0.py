def get_longer_word(word1: str, word2: str) -> str:
    len_1 = len(word1)
    len_2 = len(word2)
    if len_1 > len_2:
        return word1
    elif len_2 > len_1:
        return word2
    else:
        return word1


# do not modify below this line
print(get_longer_word("yellow", "orange"))
print(get_longer_word("red", "blue"))
print(get_longer_word("green", "blue"))
