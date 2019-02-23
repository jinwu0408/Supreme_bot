class users:
    def __init__(self, profile):
        self.name = profile.get('name')
        self.email = profile.get('email')
        self.tel = profile.get('tel')
        self.address = profile.get('address')
        self.card = profile.get('card')

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_tel(self):
        return self.tel

    def get_address(self):
        return self.address

    def get_card(self):
        return self.card
