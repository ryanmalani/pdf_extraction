import unittest
import os
from unittest.mock import patch

from scripts import splitter

class TestSplitter(unittest.TestCase):

    @patch('os.remove')
    @patch('builtins.print')
    def test_pdf_remove(self, mock_print, mock_remove):
        fname = ['file1.pdf', 'file2.pdf', 'file3.pdf']
        length = len(fname)

        splitter.pdf_remove(length)

        mock_remove.assert_called_with('../PDFs-TextExtract/split/file1.pdf')
        mock_remove.assert_called_with('../PDFs-TextExtract/split/file2.pdf')
        mock_remove.assert_called_with('../PDFs-TextExtract/split/file3.pdf')

        mock_print.assert_called_with('Deleted: ../PDFs-TextExtract/split/file1.pdf')
        mock_print.assert_called_with('Deleted: ../PDFs-TextExtract/split/file2.pdf')
        mock_print.assert_called_with('Deleted: ../PDFs-TextExtract/split/file3.pdf')

    # def test_pdf_splitter(self):
    #     split = target.pdf_splitter
    #     self.assertIs(split, len(pdf_reader.pages))

if __name__ == "__main__":
    unittest.main()