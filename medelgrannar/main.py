input = input('Skriv in en nummer sekvens: ').split()
numInput = list(map(int, input))

if len(input) >= 3:
    i = 0

    for i in range(len(input)):

        if i != 0 and i != len(input) -1:
            avg = (numInput[i] + numInput[i + 1] + numInput[i - 1]) / 3
            print(avg)


