import phonenumbers
num = input()
if phonenumbers.parse(num):
    print(True)
else:
    print(False)