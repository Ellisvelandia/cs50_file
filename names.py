# names = []

# for _ in range(3):
#   names.append(input("whats your name? "))

#   for name in sorted(names):
#     print(f"hello, {name}")
name = input("whats youe name? ")

file = open("names.txt", "a")
file.write(name)
file.close()