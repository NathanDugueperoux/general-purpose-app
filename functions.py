def handle_invalid_email(email):
    if email.endswith("@gmail.com") or email.endswith("@yahoo.com") or email.endswith("@outlook.com"):
        if email.split("@")[0] == "":
            return "invalid"
        else:
            return "valid"
    else:
        return "invalid"


def handle_invalid_password(password):
    total = 0
    special_chars = "!£$%^&*()_-+={[]}@'~#:;><,.?/|`¬"
    if len(password) >= 20:
        return "too large"
    elif len(password) <= 3:
        return "too small"
    else:
        for i in special_chars:
            if i in password:
                total += 1
        if total > 0:
            return "valid"
        else:
            return "no special chars"


def handle_encryption(word):
    chars = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    cap_chars = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz".upper()
    word = [*word]
    for i in range(len(word)):
        if word[i].isalpha():
            if word[i].islower():
                word[i] = chars[(chars.index(word[i])) + 5]
            elif word[i].isupper():
                word[i] = cap_chars[(cap_chars.index(word[i])) + 5]
        elif word[i].isdigit():
            word[i] = str(int(word[i]) + 5)
    return "".join(word)


def handle_decryption(word):
    chars = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    cap_chars = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz".upper()
    word = [*word]
    for i in range(len(word)):
        if word[i].isalpha():
            if word[i].islower():
                word[i] = chars[(chars.index(word[i])) - 5]
            elif word[i].isupper():
                word[i] = cap_chars[(cap_chars.index(word[i])) - 5]
        elif word[i].isdigit():
            word[i] = str(int(word[i]) - 5)
    return "".join(word)
