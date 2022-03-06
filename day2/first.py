with open("input2.txt") as file:
    file_source = file.read()

a = file_source.split("\n")

fwd = 'forward'
dnw = 'down'
up = 'up'

horiz = 0
depth = 0

# buf = a[0].split(' ')
# print(buf)
for i in range (len(a)):
    buf = a[i].split(' ')
    print(buf)
    match buf[0]:
        case 'forward':
            horiz += int(buf[1])
        case 'down':
            depth += int(buf[1])
        case up:
            depth -= int(buf[1])
                    

print(horiz * depth)


