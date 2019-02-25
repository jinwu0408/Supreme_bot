class Users:
    def __init__(self, profile):
        self.name = profile.get('name')
        self.email = profile.get('email')
        self.tel = profile.get('tel')
        self.address = profile.get('address')
        self.card = profile.get('card')

    def name(self):
        return self.name


    def email(self):
        return self.email


    def tel(self):
        return self.tel


    def address(self):
        return self.address


    def card(self):
        return self.card
