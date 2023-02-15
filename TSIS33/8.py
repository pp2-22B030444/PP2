class Person:

    #count_of_objects=0
    def __init__(self,first_name,last_name,age,occupation,gender,nationality):
        
        #self.count_of_objects=count_of_objects
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.occupation=occupation
        self.gender=gender
        self.nationality=nationality
        #Person.count_of_objects += 1
    def year_born(self,cur_year):
        return cur_year-self.age
    def get_name(self):
        return f'{self.first_name} {self.last_name}'
    def get_nationality(self):
        return self.nationality
    def get_age(self):
        return self.age
    def get_occupation(self):
        return self.occupation
actor1 = Person(first_name="Brad", last_name="Pitt", age=50, occupation="Actor", gender="Man", nationality="American")

print(actor1.year_born(cur_year=2023)) #Result will be   1973
print(actor1.get_name(),actor1.get_nationality(),actor1.get_age(),actor1.get_occupation())
#print(actor1.count_of_object(Person))   #Result will be  1


actor2 = Person(first_name="Tom", last_name="Cruise", age=61, occupation="Actor", gender="Man", nationality="American")

print(actor2.year_born(cur_year=2023))   #Result will be   1962

#actor2.count_of_object   #Result will be   2
