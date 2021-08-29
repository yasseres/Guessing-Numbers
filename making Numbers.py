import csv

z = 0

for x in range(10000):

    z = z + 3

    Number = z
    
    Input1 = z+5*7

    with open ("Numbers.csv", "a", newline="") as f:
        fieldnames = ["to be issued", "Result"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writerow({"to be issued" : Number, "Result" : Input1})