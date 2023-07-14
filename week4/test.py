from random import randint


minimum = int(input("Min: "))
maximum = int(input("Max: "))
n_randoms = int(input("How many random numbers? "))

output = ""
for counter in range(n_randoms):
    output += f" {randint(minimum, maximum)}"
print(output)

print()
input("Press return to continue ...")