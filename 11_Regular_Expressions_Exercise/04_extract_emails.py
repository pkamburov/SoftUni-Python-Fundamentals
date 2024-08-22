import re

sentence = input()
pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"
extracted_emails = re.findall(pattern, sentence)

for email in extracted_emails:
    print(email[0])
