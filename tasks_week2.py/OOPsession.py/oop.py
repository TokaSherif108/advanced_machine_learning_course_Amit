class person:
    person_name="TOKA"
    person_age=26
    def person_info(x):
        print("hello toka")
p1=person()
p2=person()
print(p1.person_info())
print(p1.__dict__)
print(p2.__dict__)
print(person.__dict__)