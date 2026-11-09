print("Podaj liczbe a")
a = float(input())
print("Podaj liczbe b")
b = float(input())
print("Podaj operator")
o = str(input())

if o == "+":
    print(a+b)

if o == "-":
    print(a-b)

if o == "*":
    print(a*b)

if o == "/":
    if b == 0:
        print("nie dziel przez 0")
    else:
        print(a/b)