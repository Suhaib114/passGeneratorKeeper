import pickle
import pyperclip  # For cut paste copy

master_password = input("Enter the main password: ")

if master_password == "qwertyuiop":  # master password
    account_name = input("enter account name: ")
    with open("passwordVault.pew", "br") as readfile:
        info = pickle.load(readfile)

    if account_name in info:
        pyperclip.copy(info[account_name])
        print("Password copied")
    else:
        print("Password not found")

else:
    print("Password doesn't match")