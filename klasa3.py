from pprint import pprint
class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):
        return f'{self.name!r}, {self.email!r}'


class Suplier(Contact):
    """
    Dziedziczenie po Contact
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")


c1 = Contact("Adam", "admin@wp.pl")
c2 = Contact("Piotr", "pipi@onet.pl")

print(c2)
print(c1.all_contacts)

s = Suplier('Tomek', 'tomek@gmail.com')
print(s)
s.order("kawa")
pprint(c1.all_contacts)
