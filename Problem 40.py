def integer_string(x):
    integer_list = []
    for a in range(1,x + 1):
        for b in str(a):
            integer_list.append(b)
    return ''.join(integer_list)

x = integer_string(1000000)
print(int(x[0]) * int(x[9]) * int(x[99]) * int(x[999]) * int(x[9999]) * int(x[99999]) * int(x[999999]))
