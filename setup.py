class Setup:
    def __init__(self, config):
        self.category = config.get('category')
        self.keyword = config.get('keyword')
        self.size = config.get('size')
        self.color = config.get('color')


    def category(self):
        return self.category


    def keyword(self):
        return self.keyword


    def size(self):
        return self.size


    def color(self):
        return self.color
