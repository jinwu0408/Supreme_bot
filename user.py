class users:
    def __init__(self, name, email, tel, address, card):
        self.name = name
        self.email = email
        self.tel = tel
        self.address = address
        self.card = card

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
