def remove_fourth_character(word: str) -> str:
    new_str = word[0:3]
    aft_str = word[4:]
    return new_str+aft_str



# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
