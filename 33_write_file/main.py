# text = "Hello!\nThis is some text\nHave a good rest of your day!"
text = "Nice to see you!"

# with open('test.txt', 'w') as file: # writes to the file
with open('test.txt', 'a') as file: # appends to the file
    file.write(text)