from document import Document

class Member():

    def __init__(self, last_name=None, first_name=None, gender=None, marital_status=None, prior_conventions=0,
                 company=None, job_title=None, nickname=None, twitter_handle=None, photo=None):
        self.last_name = last_name
        self.first_name = first_name
        self.gender = gender
        self.marital_status = marital_status
        self.prior_conventions = prior_conventions
        self.company = company
        self.job_title = job_title
        self.nickname = nickname or first_name
        self.twitter_handle = twitter_handle
        self.photo = photo

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

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def create_letter(self):
        Document(document="letter", result=self.result_string, context={'member': self}).render()

    def create_letter2(self):
        Document(document="letter2", result=self.result_string, context={'member': self}).render()

    def create_badge(self):
        Document(document="badge", result=self.result_string, context={'member': self}).render()

    def create_badge2(self):
        Document(document="badge2", result=self.result_string, context={'member': self}).render()