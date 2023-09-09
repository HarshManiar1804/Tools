#!/usr/bin/env python3
import hashlib
import requests

def check_password(sha1hash):
    url = 'https://raw.githubusercontent.com/iryndin/10K-Most-Popular-Passwords/master/passwords.txt'
    response = requests.get(url)
    passlist = response.text

    for password in passlist.split('\n'):
        hashguess = hashlib.sha1(password.encode('utf-8')).hexdigest()
        if hashguess == sha1hash:
            print(f"[+] The password is: {password}")
            return

    print("Password is not in the list")

def main():
    sha1hash = input("[*] Enter the hash value of the password: ")
    check_password(sha1hash)

if _name_ == "_main_":
    main()