from unittest import TestCase
from unittest.mock import patch
from dir_helpers import get_all_files

class TestGetAllFiles(TestCase):
    @patch("dir_helpers.os")
    def test_invalid_directory(self, mocked_os):
        mocked_os.path.isdir.return_value = False
        with self.assertRaises(ValueError):
            [f for f in get_all_files("i-am-not-a-directory-for-sure")]

    @patch("dir_helpers.os")
    def test_valid_directory(self, mocked_os):
        mocked_os.path.isdir.return_value = True
        mocked_os.walk.return_value = [
            (".", None, ["file1.txt"]),
            ("./nested", None, ["file2.txt"]),
            ("./nested/twice", None, ["file3.txt"]),
            ("./nested/many/times", None, ["file4.txt"]),
        ]
        def mock_join(a, b):
            return f"{a}/{b}"
        mocked_os.path.join.side_effect = mock_join
        
        files = [f for f in get_all_files("i-am-a-directory")]
        assert files == ['./file1.txt', './nested/file2.txt', './nested/twice/file3.txt', './nested/many/times/file4.txt']
            
