import classmodule

#ooha object
p1 = classmodule.MyDetails("ooha", "guntupalli", 26, "cook")
print("My Name is", p1.first_name, p1.last_name, "My age is", p1.age)
p1.employer("Intelnet")

#sandeep object
p1 = classmodule.MyDetails("sandeep", "guntupalli", 32, "Farmer")
p1.employer("ericsson")
p1.age = 31
print(p1.age)
a1 = classmodule.Person("John", 36)
a1.myfunc()

a2 = classmodule.Person("Sandeep", 32)
a2.myfunc()