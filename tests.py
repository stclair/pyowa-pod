import unittest
import mock

from member import Member
from document import Document

class DocumentTests(unittest.TestCase):

    def test_can_be_initialized_with_result(self):
        doc = Document(result="test")
        self.assertEqual("test", doc.result)

    def test_result_file_property_returns_result_dot_odt_in_results_folder(self):
        doc = Document(result="test")
        self.assertEqual("results/test.odt", doc.result_file)

    def test_can_be_initialized_with_document(self):
        doc = Document(document="test")
        self.assertEqual("test", doc.document)

    def test_document_file_property_returns_document_dot_odt_in_documents_folder(self):
        doc = Document(document="test")
        self.assertEqual("documents/test.odt", doc.document_file)

    def test_can_be_initialized_with_context(self):
        doc = Document(context="test")
        self.assertEqual("test", doc.context)

    @mock.patch("document.Renderer")
    @mock.patch("os.remove", mock.Mock())
    def test_call_pod_renderer_with_document_file_and_context_and_result_file_in_render_then_call_run(self, renderer):
        doc = Document(context="context")
        doc.document_file = "document"
        doc.result_file = "result"
        doc.render()
        renderer.assert_called_once_with("document", "context", "result")
        renderer.return_value.run.assert_called_once_with()

    @mock.patch("document.Renderer", mock.Mock())
    @mock.patch("os.remove")
    def test_remove_result_file_before_rendering_in_render(self, os_remove):
        doc = Document()
        doc.result_file = "test"
        doc.render()
        os_remove.assert_called_once_with("test")


class MemberTests(unittest.TestCase):

    def test_can_be_initialized_with_name(self):
        member = Member(name="test")
        self.assertEqual("test", member.name)

    @mock.patch("member.Document")
    def test_create_letter(self, doc):
        member = Member()
        member.create_letter()
        doc.assert_called_once_with("letter", member.name, member)
        doc.return_value.render.assert_called_once_with()

class FunctionalTests(unittest.TestCase):

    def test_render_letter(self):
        member = Member(name="Wes")
        member.create_letter()