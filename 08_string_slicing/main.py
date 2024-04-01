name = "Alex Williams"

# [start:stop:step]

# first_name = name[0:4]
first_name = name[:4]
# last_name = name[5:13]
last_name = name[5:]
# funky_name = name[0:13:2]
funky_name = name[::2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website1 = "https://google.com"
website2 = "https://wikipedia.com"

slice = slice(8, -4)

print(website1[slice])
print(website2[slice])