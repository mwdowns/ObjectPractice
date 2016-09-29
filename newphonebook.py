
class Contact (object):
    def __init__(self, name, home, work, email):
        self.name = name
        self.home = home
        self.work = work
        self.email = email


class Phonebook (object):
    def __init__ (self):
        self.contacts = {}

    def add_contact(self):
        name = str.upper(raw_input("Name? "))
        home = str.upper(raw_input("Home number? "))
        work = str.upper(raw_input("Work number? "))
        email = str.lower(raw_input("Email address? "))
        contact = Contact(name, home, work, email)
        self.contacts[name] = contact

    def delete_contact(self):
        destroy = str.upper(raw_input("Which contact would you like to delete? "))
        if destory == self.contacts[name]:
            del self.contacts[name]
        else:
            print "Sorry, %s is not in the Phonebook" % destroy

    def list_contacts(self):
        for i in self.contacts:
            print "%s -- Home: %s, Work: %s, email: %s" % (self.contacts[name], self.contacts[home], self.contacts[work], self.contacts[email])
    #
    # def search



def runPhonebook():

    print """

    Electronic Phone Book
    =====================
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Save all entries
    6. Quit
    """
    p = Phonebook()

    option = raw_input("What do you want to do (1 -6)? ")

    if option == "1":
        p.add_contact()
    elif option == "2":
        p.add_contact()
    elif option == "3":
        p.delete_contact()
    elif option == "4":
        p.list_contacts()
    # elif option == "5":
    #
    # else:

runPhonebook()
