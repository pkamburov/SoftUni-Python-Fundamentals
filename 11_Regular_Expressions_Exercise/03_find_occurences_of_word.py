import re

sentence = input()
word = input()
pattern = fr"(?i)\b{word}\b"
matches = re.findall(pattern, sentence)
print(len(matches))
