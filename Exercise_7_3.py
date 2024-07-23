from faker import Faker
fake = Faker('pl_PL')

class Card:
    def __init__(self, first_name, last_name, address, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        
        

    @property
    def label_length(self):
        return len(self.first_name + ' ' + self.last_name)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.address} {self.email} '

Card001 = Card(first_name=fake.first_name(), last_name=fake.last_name(), address=fake.address(), email=fake.email())
Card002 = Card(first_name=fake.first_name(), last_name=fake.last_name(), address=fake.address(), email=fake.email())
Card003 = Card(first_name=fake.first_name(), last_name=fake.last_name(), address=fake.address(), email=fake.email())
Card004 = Card(first_name=fake.first_name(), last_name=fake.last_name(), address=fake.address(), email=fake.email())
Card005 = Card(first_name=fake.first_name(), last_name=fake.last_name(), address=fake.address(), email=fake.email())

list_of_cards = [Card001, Card002, Card003, Card004, Card005]
by_first_name = sorted(list_of_cards, key=lambda Card: Card.first_name)
by_last_name = sorted(list_of_cards, key=lambda Card: Card.last_name)
by_email = sorted(list_of_cards, key=lambda Card: Card.email)

print(Card001)

class BaseContact(Card):
    def __init__(self, phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.phone = phone
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.address} {self.email} {self.phone}'
        
    
    def contact(self):
        print(f'Wybieram numer +48 {self.phone} i dzwonię do {self.first_name} {self.last_name}')

BaseContactCard001 = BaseContact(first_name='Klaudia', last_name='Nowak', address='Boćki 35', email='example@wp.pl', phone='600524525')
print(BaseContactCard001)
print(BaseContactCard001.label_length)
BaseContact.contact(BaseContactCard001)
#BaseContactCard001 = BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), address=fake.address(), email=fake.email(), phone=fake.phone())

class BusinessContact(Card):
    def __init__(self, job, company, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.work_phone = work_phone
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.address} {self.email} {self.job} {self.company} {self.work_phone}'



    def contact(self):
        print(f'Wybieram numer +48 {self.work_phone} i dzwonię do {self.first_name} {self.last_name}')

BusinessContactCard001 = BusinessContact(first_name='Klaudia', last_name='Nowak', address='Boćki 35', email='example@wp.pl', job='Rolnik', company='PGR', work_phone='600524526')
print(BusinessContactCard001)
print(BusinessContactCard001.label_length)
BusinessContact.contact(BusinessContactCard001)

list_of_baseContact = []
list_of_businessContact = []
def create_contacts(name_of_class, quantity):
    if name_of_class == BaseContact:
        for i in range(quantity):
            BaseContact(first_name=fake.first_name(), last_name=fake.last_name(),
                                                 address=fake.address(), email=fake.email(), phone=fake.phone_number())
    elif name_of_class == BusinessContact:
        for i in range(quantity):
            BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(),
                                                         address=fake.address(), email=fake.email(), job=fake.job(),
                                                         company=fake.company(), work_phone=fake.phone_number())

    pass

create_contacts(BaseContact, 2)
create_contacts(BusinessContact, 3)
