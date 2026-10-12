print("Program starting.")
print()
print("Check multiplicative persistence.")
i = int(input("Insert an integer: "))
steps = 0
while i >= 10:
    div = 1
    while div * 10 <= i:
        div = div * 10
    number = i
    product = 1
    first = True
    while div >= 1:
        digit = number // div
        number = number % div
        div = div // 10
        if not first:
            print(" * ", end="")
        print(digit, end="")
        product = product * digit
        first = False
    print(" =", product)
    i = product
    steps += 1
print("No more steps.")
print()
print("This program took", steps, "step(s)")
print()
print("Program ending.")