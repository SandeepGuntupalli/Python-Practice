class MyDetails:
    def __init__(sandeep, f_name, l_name, age, work):
        sandeep.first_name = f_name
        sandeep.last_name = l_name
        sandeep.age = age
        sandeep.work = work

    def employer(sandeep, company):
        if sandeep.first_name == "sandeep":
            print("My Name is", sandeep.first_name, "My Employer is", company, "By interest I am a", sandeep.work)
        if sandeep.first_name == "ooha":
            print("My Employer is", company, "By interest I am a", sandeep.work)


class Person:
    def __init__(sandeep, name, age):
        sandeep.name = name
        sandeep.age = age

    def myfunc(sandeep):
        if sandeep.name == "Sandeep":
            print("Hello my name is " + sandeep.name)
        else:
            print("Sorry I don't know your name")

