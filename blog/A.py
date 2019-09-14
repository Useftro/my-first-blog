a = int(input())
b = int(input())

if a**b < b**a:
    print("<")
elif a**b > b**a:
    print(">")
else:
    print("=")
