#!/usr/bin/python3

x = 0
y = 1
i = 1
while i<=10:
    i += 1
    print(x,y)
    x = x + y
    y = x + y
else:
	print("End of the while loop")
