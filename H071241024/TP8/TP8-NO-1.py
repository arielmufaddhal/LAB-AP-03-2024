import re

def validate_string(str):
    if len(str) != 45:
        return False
    
    first_40 = str[:40]
    last_5 = str[40:]
    
    pattern_40 = r'^[a-zA-Z02468]{40}$'
    pattern_5 = r'^[\s13579]{5}$'
    
    if not re.match(pattern_40, first_40):
        return False
    if not re.match(pattern_5, last_5):
        return False
    return True

def main():
    str = input("Masukkan str: ")
    result = validate_string(str)
    print("True" if result else "False")

main()