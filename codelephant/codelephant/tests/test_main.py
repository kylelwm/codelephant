import json
from unittest import TestCase
from unittest.mock import patch
from main import process_directory


class TestProcessDirectory(TestCase):
    @patch("main.get_all_files")
    def test_invalid_directory(self, mocked_get_all_files):
        mocked_get_all_files.side_effect = ValueError("Kaboom!")
        with self.assertRaises(SystemExit):
            process_directory("any_directory")

    @patch("main.get_all_files")
    def test_no_files(self, mocked_get_all_files):
        mocked_get_all_files.return_value = []
        assert process_directory("any_directory") == json.dumps({
            "summary": {},
            "results": []
        }, indent=4)



    @patch("main.get_all_files")
    def test_files_not_in_known_extensions(self, mocked_get_all_files):
        mocked_get_all_files.return_value = ["script.go", "main.ts", "calculator.rb"]
        assert process_directory("any_directory") == json.dumps({
            "summary": {},
            "results": []
        }, indent=4)


    @patch("main.get_all_files")
    def test_valid_directory(self, mocked_get_all_files):
        mocked_get_all_files.return_value = [
            "/path/to/some/project/backend/config/manage.py",
            "/path/to/some/project/backend/requirements.txt",
            "/path/to/some/project/src/app/Application.js",
            "/path/to/some/project/src/app/index.js",
            "/path/to/some/project/src/components/StatusBar/Container/Container.js",
            "/path/to/some/project/src/components/StatusBar/Container/index.js",
            "/path/to/some/project/src/index.js",
            "/path/to/some/project/Makefile",
            "/path/to/some/project/README.md",
        ]
        assert process_directory("any_directory") == json.dumps({
            "summary": {
                "python": 0.142857,
                "js": 0.714286,
                "make": 0.142857
            },
            "results": [
                {
                    "path": "/path/to/some/project/backend/config/manage.py",
                    "language": "python"
                },
                {
                    "path": "/path/to/some/project/src/app/Application.js",
                    "language": "js"
                },
                {
                    "path": "/path/to/some/project/src/app/index.js",
                    "language": "js"
                },
                {
                    "path": "/path/to/some/project/src/components/StatusBar/Container/Container.js",
                    "language": "js"
                },
                {
                    "path": "/path/to/some/project/src/components/StatusBar/Container/index.js",
                    "language": "js"
                },
                {
                    "path": "/path/to/some/project/src/index.js",
                    "language": "js"
                },
                {
                    "path": "/path/to/some/project/Makefile",
                    "language": "make"
                }
            ]
        }, indent=4)
