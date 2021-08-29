# Guessing-Numbers
My aim is to make an ai that can find out what happend to a number.
So its my first time using github. I dont know if anyone will see this.




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
        
        
       
As you can Imagine the Code gives the following Numbers


3,38
6,41
9,44
12,47
15,50
18,53
21,56
24,59
27,62

I want an ai to read these Numbers and find a pattern. What happend to 3 that it ended up 38, What happend to 6 that it ended up 41... and so on.

I tried for a few hours and could not get anywhere. If someone could direct me into the right direction, that would be amazing
        
