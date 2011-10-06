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
    @mock.patch("os.path.isfile")
    @mock.patch("os.remove")
    def test_remove_result_file_before_rendering_in_render(self, os_remove, os_isfile):
        os_isfile.return_value = True
        doc = Document()
        doc.result_file = "test"
        doc.render()
        os_remove.assert_called_once_with("test")


class MemberTests(unittest.TestCase):

    def test_can_be_initialized_with_fields(self):
        member = Member(last_name="last", first_name="first", gender="male", marital_status="married")
        self.assertEqual("last", member.last_name)
        self.assertEqual("first", member.first_name)
        self.assertEqual("male", member.gender)
        self.assertEqual("married", member.marital_status)

    def test_get_result_string(self):
        member = Member(last_name="last", first_name="first")
        self.assertEqual("last-first", member.result_string)

    @mock.patch("member.Document")
    def test_create_letter(self, doc):
        member = Member()
        member.create_letter()
        doc.assert_called_once_with(document="letter", result=member.result_string, context={'member': member})
        doc.return_value.render.assert_called_once_with()

    def test_member_title_based_on_gender(self):
        member = Member(gender="male", marital_status="married")
        self.assertEqual("Mr.", member.title)

class FunctionalTests(unittest.TestCase):

    def test_render_letter(self):
        member = Member(last_name="St.Clair", first_name="Wes", gender="male", marital_status="married")
        member.create_letter()

    def test_letter2_no_prior_conventions(self):
        member = Member(last_name="St.Clair", first_name="Wes", gender="male", marital_status="married")
        member.create_letter2()

    def test_badge(self):
        member = Member(last_name="St.Clair", first_name="Wesley", nickname="Wes", company="The IMT Group",
                        job_title="IT Manager", twitter_handle="@wes_stclair" )
        member.create_badge()

    def test_badge2(self):
        member = Member(last_name="St.Clair", first_name="Wesley", nickname="Wes", company="The IMT Group",
                        job_title="IT Manager", twitter_handle="@wes_stclair", photo="me.jpg" )
        member.create_badge2()