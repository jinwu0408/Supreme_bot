class Users:
    def __init__(self, profile):
        self.name = profile.get('name')
        self.email = profile.get('email')
        self.tel = profile.get('tel')
        self.address = profile.get('address')
        self.card = profile.get('card')

    @property
    def name(self):
        return self.name

    @property
    def email(self):
        return self.email

    @property
    def tel(self):
        return self.tel

    @property
    def address(self):
        return self.address
    
    @property
    def card(self):
        return self.card
