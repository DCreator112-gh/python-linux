import time

from guibhvhmvmhg import *

print("starting penguin os")
time.sleep(5)


def ls():
    files = ""
    for i in FILES:
        files += i + " "
    return files


users = {"root": "toor", "dcreator112": "password123", "fred": "hi"}
print("penguin started who are you")
user = input()
if user not in users:
    print("no")
    kernel_panic()

print("ok what password")

password = input()
if users[user] != password:
    print("no")
    kernel_panic()

print("welcome")
FILES = {"hi.txt": "linux in python is cool"}
commands = {"ls": ls}
command = input("->")
if command not in commands:
    print("no")
    kernel_panic()
print(commands[command]())
