import re

def validate_phone_number(number):
    if not re.match(r"^01[016789][1-9]\d{6,7}$", number):
        return False
    return True


print(validate_phone_number('01012341234'))
print(validate_phone_number('010123412'))
print(validate_phone_number('01012341234a'))
