with open("input.txt") as file:
    file_source = file.read()

    a = file_source.split("\n")
dec = 0
for i in range (len(a) - 1):
    print ("index = ", i, "inc = ", inc)
    if a[i] > a[i + 1]:
        dec += 1
print(len(a) - dec)
