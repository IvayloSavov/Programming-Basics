role = (input())


is_admin = role == "Admin"
is_secondary_admin = role == "Secondary admin"
is_user = role == "User"
if is_admin:
    print("Hello admin")
if is_secondary_admin:
    print("Hello, you don't have full rights")
elif is_user:
    print("hello, you can't open this page")