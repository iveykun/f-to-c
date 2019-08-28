temp = int(input("Temperature?"))
scale = str(input("F or C"))

if scale is "f":
    print(temp, "F is", (temp-32)*(5/9), "C")
if scale is "c":
    print(temp, "C is", (temp)*(9/5)+32, "F")
