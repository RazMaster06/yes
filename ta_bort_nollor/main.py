number = str(input("Vilket tal vill du förenkla?: "))

def cutter():
    y = number.strip("0")
    return y

x = cutter()

print(x)