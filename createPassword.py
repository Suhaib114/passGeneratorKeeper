import random
import pickle  # for creating binary file

info = {}  # creating a dictionary

with open("passwordVault.pew", "br") as readfile:  # read the old file
    info = pickle.load(readfile)  # get info from the file


s = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBMN1234567890!@#&()?/"  # strings that are going to use to generate password
len_password = int(input("enter the number of letters you need in password: "))

password = "".join(random.sample(s, len_password))  # the result comes out as list have to make it string
print(password)

answer = input("Would you like to keep this password? (Y/N)").upper()  # upper for capital letter
if "Y" in answer:
    account_name = input('Enter account name: ')
    info[account_name] = password  # save the account name and password in the dictionary
    print(info)
    with open("passwordVault.pew","bw") as filewrite:   # file type
        pickle.dump(info, filewrite, protocol=2)  # Create portable serialized representations




else:
    print("OK")