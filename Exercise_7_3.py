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
        return f'{self.first_name} {self.last_name} {self.email}'

Card001 = Card(first_name=fake.first_name(), last_name=fake.last_name(), address=fake.address(), email=fake.email())
Card002 = Card(first_name=fake.first_name(), last_name=fake.last_name(), address=fake.address(), email=fake.email())
Card003 = Card(first_name=fake.first_name(), last_name=fake.last_name(), address=fake.address(), email=fake.email())
Card004 = Card(first_name=fake.first_name(), last_name=fake.last_name(), address=fake.address(), email=fake.email())
Card005 = Card(first_name=fake.first_name(), last_name=fake.last_name(), address=fake.address(), email=fake.email())

list_of_cards = [Card001, Card002, Card003, Card004, Card005]
by_first_name = sorted(list_of_cards, key=lambda Card: Card.first_name)
by_last_name = sorted(list_of_cards, key=lambda Card: Card.last_name)
by_email = sorted(list_of_cards, key=lambda Card: Card.email)

class BaseConctact(Card):
    def __init__(self, phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.phone = phone

class BusinessContact(Card):
    def __init__(self, job, company, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.work_phone = work_phone


