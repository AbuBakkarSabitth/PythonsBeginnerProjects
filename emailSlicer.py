email = input("enter your email :")



username = email[:email.index("@")]

domain = email[email.index("@")+1:]
print(f"Your username is {username} and domain is {domain}")
