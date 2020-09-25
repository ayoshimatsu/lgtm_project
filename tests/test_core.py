import unittest
import os
import sys

sys.path.append(os.getcwd())

class LgtmTest(unittest.TestCase):
    def test_lgtm(self):
        from lgtm.core import lgtm
        self.assertIsNone(lgtm())

