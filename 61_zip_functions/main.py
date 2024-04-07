usernames = ["Alex", "Williams", "Mister"]
passwords = ("password", "abc123", "guest")
login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

# users = zip(usernames, passwords)
# users = list(zip(usernames, passwords))
# users = dict(zip(usernames, passwords))
users = zip(usernames, passwords, login_date)

print(type(users))

for i in users: print(i)

# for key, value in users.items():
#     print(key, value, sep=":")
