username = input()
password = input()

temp_password = ""
while temp_password != password:
    temp_password = input()
print(f"Welcome {username}!")