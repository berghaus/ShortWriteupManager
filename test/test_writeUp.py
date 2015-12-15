from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest
from writeup.writeup import WriteUp
from datetime import date

class TDDWriteUp(unittest.TestCase):

    def test_write_up_stores_filename(self):
        write_up = WriteUp("test.tex")
        result = write_up._fileName
        self.assertEqual("test.tex", result)

    def test_write_up_parses_title(self):
        write_up = WriteUp("test.tex")
        self.assertEqual('Manipulation of Triangular and Symmetric Matrices',write_up.title)

    def test_write_up_parses_author(self):
        write_up = WriteUp("test.tex")
        result = write_up.author
        self.assertEqual("W. Hart", result)

    def test_write_up_parses_ID(self):
        write_up = WriteUp("test.tex")
        result = write_up.ID
        self.assertEqual("F112", result)

    def test_write_up_parses_keywords(self):
        write_up = WriteUp("test.tex")
        self.assertIn("operation",write_up.keywords)
        self.assertIn("symmetric",write_up.keywords)
        self.assertIn("triangular",write_up.keywords)
        self.assertIn("matrix",write_up.keywords)
        self.assertIn("number",write_up.keywords)
        self.assertIn("zero",write_up.keywords)
        self.assertIn("complex",write_up.keywords)
        self.assertIn("analytic",write_up.keywords)
        self.assertIn("function",write_up.keywords)
        self.assertIn("logarithmic",write_up.keywords)
        self.assertIn("residue",write_up.keywords)

    def test_write_up_parses_routines(self):
        write_up = WriteUp("test.tex")
        self.assertIn("trchul",write_up.routines)
        self.assertIn("trchlu",write_up.routines)
        self.assertIn("trsmul",write_up.routines)
        self.assertIn("trsmlu",write_up.routines)
        self.assertIn("trinv",write_up.routines)

    def test_write_up_parses_library(self):
        write_up = WriteUp("test.tex")
        self.assertEqual("kernlib",write_up.library)

    def test_write_up_parses_language(self):
        write_up = WriteUp("test.tex")
        self.assertEqual("fortran",write_up.language)

    def test_write_up_parses_submitter(self):
        write_up = WriteUp("test.tex")
        self.assertEqual("Waggleton P. Tallylicker",write_up.submitter)

    def test_write_up_parses_submitted(self):
        write_up = WriteUp("test.tex")
        self.assertEqual(date(1975,1,1),write_up.submitted)

    def test_write_up_parses_revised(self):
        write_up = WriteUp("test.tex")
        self.assertEqual(date(1986,12,12),write_up.revised)


if __name__ == "__main__":
    unittest.main()
