import re

def valid(setring):
    pattern = r"^[a-zA-Z02468]{40}[13579\s]{5}$"
    
    if  re.match(pattern, setring):
        return "True"
    else:
        return "False"

setring = input("masukkan string: ")
print(valid(setring))
