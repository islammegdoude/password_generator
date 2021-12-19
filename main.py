import string
import random

list1 = list(string.ascii_lowercase)
list2 = list(string.ascii_uppercase)
list3 = list(string.digits)
list4 = list(string.punctuation)

char_numb = input("how many characters for the Password :")

while True:
    try:
        char_numb = int(char_numb)
        if char_numb < 6:
            print("you need set a least 6 characters !! ")
            char_numb = input("how many characters for the Password :")
        else:
            break
    except:
        print("Please enter numbers only !!")
        char_numb = input("how many characters for the Password :")
random.shuffle(list1)
random.shuffle(list2)
random.shuffle(list3)
random.shuffle(list4)
part1 = int(char_numb * (30 / 100))
part2 = int(char_numb * (20 / 100))

password = []

for i in range(part1):
    password.append(list1[i])
    password.append(list2[i])
for i in range(part2):
    password.append(list3[i])
    password.append(list4[i])
if (part1 + part2) * 2 != char_numb:
    password.append(list1[i])
random.shuffle(password)
password = "".join(password[0:])
print("Your Password is :", password)
