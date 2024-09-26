from sys import argv

print("The number of command line arguemtn", len(argv))
print("The command line arguments are: ", argv)
print(type(argv))

for x in argv:
    print(x)