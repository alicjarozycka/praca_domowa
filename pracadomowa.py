def nwd(a, b):
    while a != b:
        if a > b:
            a = a - b
        if a < b:
            b = b - a
    return b  # nie ma znaczenia jak zwrocimy 'a' lub 'b'


def nww(a, b):
    return (a * b) / nwd(a, b)


x = int(input("Podaj pierwszą liczbę:"))
y = int(input("Podaj drugą liczbę:"))
print("NWD: ", nwd(x, y))
print("NWW: ", nww(x, y))
