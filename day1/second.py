with open("input2.txt") as file:
    file_source = file.read()

    a = file_source.split("\n")
    A = 0
    B = 0
    count = 0
    for i in range (len(a) - 3):
        print('i', A, B)
        A = int(a[i]) + int(a[i + 1]) + int(a[i + 2])
        B = int(a[i + 1]) + int(a[i + 2]) + int(a[i + 3])
        if A < B:
            print('A < B')
            count += 1



    print(count)