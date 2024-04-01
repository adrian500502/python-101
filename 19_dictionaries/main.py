capitals = {"USA":"Washington DC", "India":"New Dehli", "China":"Beijing", "Russia":"Moscow"}
capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Washington"})
capitals.pop("China")
# capitals.clear()

print(capitals)
print(capitals["Russia"])
print(capitals.get("Germany")) # won't break the program, results in None
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key,value in capitals.items():
    print(key, value)