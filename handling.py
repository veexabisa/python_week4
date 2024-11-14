file = open("demo.txt", "r")
print(file.read())

file = open("demo.txt", "a")
file.write("Updating with some new content")
file.close()

user = input("Please type the name of the file ")
try:
    with open("demo.txt") as file:
        data = file.read()
except FileNotFoundError:
    print("Something went wrong with opening the file")