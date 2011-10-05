from document import Document

class Member():

    def __init__(self, last_name=None, first_name=None, gender=None, marital_status=None):
        self.last_name = last_name
        self.first_name = first_name
        self.gender = gender
        self.marital_status=marital_status

    @property
    def result_string(self):
        return "%s-%s" % (self.last_name, self.first_name)

    @property
    def title(self):
        titles = {("male", "married"): "Mr.",
                  ("male", "single"): "Mr.",
                  ("female", "married"): "Mrs.",
                  ("female", "single"): "Miss",}
        return titles[(self.gender, self.marital_status)]

    def create_letter(self):
        Document(document="letter", result=self.result_string, context={'member': self}).render()