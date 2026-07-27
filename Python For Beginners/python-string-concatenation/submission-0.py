def concatenate(s1: str, s2: str) -> str:
    conc_str = s1 + s2
    str_len = len(conc_str)

    if str_len > 10:
        return "Too long!"
    else:
        return conc_str



# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
