import os

from appy.pod.renderer import Renderer

class Document():

    def __init__(self, document=None, result=None, context=None):
        self.document = document
        self.result = result
        self.context = context

    @property
    def result_file(self):
        return "results/%s.odt" % self.result

    @property
    def document_file(self):
        return "documents/%s.odt" % self.document

    def render(self):
        if os.path.isfile(self.result_file):
            os.remove(self.result_file)
        renderer = Renderer(self.document_file, self.context, self.result_file)
        renderer.run()