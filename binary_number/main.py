print("Den här konverteraren ger det binära talet som är större än det du skriver in")
number = int(input("Vad för tal vill du räkna ut?: "))
bin_number = bin(number)

x = True
i = number + 1

while x == True:
    
    if bin(i).count("1") == bin_number.count("1"):
        print(i)
        break
    
    i += 1

