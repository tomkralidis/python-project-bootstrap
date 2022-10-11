# =================================================================
#
# Author: Firstname Lastname <email-address>
#
# Copyright (c) YYYY Firstname Lastname
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================

import os
import unittest

TESTDATA_DIR = os.path.dirname(os.path.realpath(__file__))


def get_abspath(filepath):
    """helper function to facilitate absolute test file access"""

    return os.path.join(TESTDATA_DIR, filepath)


def msg(test_id, test_description):
    """convenience function to print out test id and desc"""
    return f'{test_id}: {test_description}'


class FooTest(unittest.TestCase):
    """Test suite for package Foo"""
    def setUp(self):
        """setup test fixtures, etc."""
        print(msg(self.id(), self.shortDescription()))

    def tearDown(self):
        """return to pristine state"""
        pass

    def test_smoke(self):
        """Simple Smoke Test"""
        # test assertions go here
        self.assertEquals(1, 1, 'Expected equality')


if __name__ == '__main__':
    unittest.main()
