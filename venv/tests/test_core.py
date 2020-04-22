import unittest


class LgtmTest(unittests.TestCase):
    def test_lgtm(self):
        from lgtm.core import lgtm
        self.assertIsNone(lgtm())