from faker import Faker
fake = Faker('pl_PL')

class Card:
    def __init__(self, first_name, last_name, company, job, address, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.job = job
        self.address = address
        self.email = email

    @property
    def label_length(self):
    return len(self.first_name + ' ' + self.last_name)


