""" A password length checker """


username = input('Enter your username?')
password = input('Enter your password.')

pass_length = len(password)
star_pass = '*' * pass_length
print(f"{username}, your password {star_pass} is {pass_length} long.")
