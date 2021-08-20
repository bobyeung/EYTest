import re
#import sys # could be used for terminal arguments

def validate(cardNum):
    regex1 = re.search(r"^[456][0-9]{3}(-?)[0-9]{4}\1[0-9]{4}\1[0-9]{4}$", cardNum)
    regex2 = re.search(r"([0-9])\1{4}", cardNum)

    if (regex1 and not regex2):
        return True
    else:
        return False

""" 
# seems cannot check EOL in the end
cardNum1 = "1144-4341-1234-1234"
cardNum2 = "4144-4744-1234-12344"
cardNum3 = "4144-1234-[341-7234"
cardNum4 = "4144443423417234"
cardNum5 = "4234 5678 9098 7654"
cardNum6 = "4144444012341234"
cardNum7 = "4144-14401234-1234"
cardNum7 = "4144-1440-1234-1234"

print(validate(cardNum1))
print(validate(cardNum2))
print(validate(cardNum3))
print(validate(cardNum4))
print(validate(cardNum5))
print(validate(cardNum6))
print(validate(cardNum7))
"""