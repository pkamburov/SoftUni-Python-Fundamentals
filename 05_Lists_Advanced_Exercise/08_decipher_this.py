def decipher(word):
    deciphered = ""
    for part in word:
        code = ""
        text = ""
        for i in part:
            if i.isdigit():
                code += i
            else:
                text += i
        new_part = chr(int(code)) + text
        if len(new_part) > 2:
            deciphered_part = new_part[0] + new_part[-1] + new_part[2: -1] + new_part[1]
        else:
            deciphered_part = new_part
        if part != word[-1]:
            deciphered += deciphered_part + " "
        else:
            deciphered += deciphered_part
    return deciphered


message = input().split()
print(decipher(message))
