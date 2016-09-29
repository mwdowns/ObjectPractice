class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.uniques = []

    def greet(self, other_person):
        self.greeting_count += 1
        print "Hello %s, I am %s" % (other_person.name, self.name)
        if other_person.name not in self.uniques:
            self.uniques.append(other_person.name)
        else:
            pass

    def print_info(self):
        print "%s's email is %s and phone number is %s" % (self.name, self.email, self.phone)

    def add_a_friend(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        print len(self.friends)

    def greetings_count(self):
        print self.greeting_count

    def __repr__(self):
        return "" % (self.name, self.email, self.phone)

    def unique_greets(self):
        print len(self.uniques)


sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
billy = Person("Billy", "billy@yahoo.com", "778-448-5743")


sonny.greet(jordan)
sonny.greet(jordan)
sonny.unique_greets()
#jordan.greet(sonny)
sonny.greet(billy)
sonny.unique_greets()
# sonny.greetings_count()
# jordan.greetings_count()


# print "Sonny's email is %s and phone is %s" % (sonny.email, sonny.phone)
# print "Jordan's email is %s and phone is %s" % (jordan.email, jordan.phone)
# sonny.print_info()
#
# jordan.friends.append(sonny)
# sonny.friends.append(jordan)
# jordan.add_a_friend(sonny)
# jordan.num_friends()



# class Cars(object):
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def print_info(self):
#         print "%s %s %s" % (self.year, self.make, self.model)
#
# car = Cars("Nissan", "Leaf", "2015")
#
# car.print_info()
