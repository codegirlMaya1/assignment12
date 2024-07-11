import re

texts = "Emails: user1@domain.com, user-2@exclude.com , user3@domain.com"

for text in texts:
        texts = texts.strip()
        texts = re.sub(r'\w*(?:[\.\-]\w+)@[A-Za-z]*\.?[A-Za-z0-9]*', "", texts)       
        print(texts) 
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", texts)          

print(emails)
