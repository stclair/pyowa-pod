from document import Document

class Member():

    def __init__(self, name=None):
        self.name = name

    def create_letter(self):
        Document("letter", self.name, self).render()